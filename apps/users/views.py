from django.urls import reverse_lazy
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from .models import User
from rest_framework import status
from apps.users.serializers import *
# Create your views here.

class UserAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRegisterAPI(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = serializer.save()

        return Response({
            'user': UserSerializer(user_data['user']).data,
            'refresh': user_data['refresh'],
            'access': user_data['access'],
            'transaction_url': reverse_lazy('transaction-history')
        }, status=status.HTTP_201_CREATED)