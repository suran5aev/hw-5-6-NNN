from rest_framework import serializers
from apps.coins.models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(source='sender.username')
    receiver = serializers.CharField(source='receiver.username')

    class Meta:
        model = Transaction
        fields = ['sender', 'receiver', 'amount', 'timestamp']
