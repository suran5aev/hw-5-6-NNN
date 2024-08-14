from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from apps.users.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.utils import timezone

User = get_user_model()

class TransferCoinsView(APIView):
    def post(self, request):
        sender = request.user
        receiver_username = request.data.get('receiver')
        amount = request.data.get('amount')

        try:
            receiver = User.objects.get(username=receiver_username)
        except User.DoesNotExist:
            return Response({'error': 'Получатель не найден'}, status=status.HTTP_404_NOT_FOUND)

        if sender.profile.balance < int(amount):
            return Response({'error': 'Недостаточно монет для передачи'}, status=status.HTTP_400_BAD_REQUEST)

        sender.profile.balance -= int(amount)
        receiver.profile.balance += int(amount)
        sender.profile.save()
        receiver.profile.save()

        transaction = Transaction.objects.create(sender=sender, receiver=receiver, amount=int(amount))

        return Response({'message': 'Монеты успешно переданы'}, status=status.HTTP_200_OK)

class BurnCoinsView(APIView):
    def post(self, request):
        users = User.objects.all()
        current_date = timezone.now().date()

        for user in users:
            # Если дата текущая и последний день месяца - сжигаем монеты
            if current_date.day == current_date.days_in_month:
                user.profile.balance = 0
                user.profile.save()

        return Response({'message': 'Монеты успешно сожжены'}, status=status.HTTP_200_OK)



class TransactionHistoryView(ListAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        user = self.request.user
        return Transaction.objects.filter(sender=user) | Transaction.objects.filter(receiver=user)
