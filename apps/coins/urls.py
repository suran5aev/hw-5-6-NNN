from django.urls import path
from .views import TransferCoinsView, TransactionHistoryView, BurnCoinsView

urlpatterns = [
    path('transfer/', TransferCoinsView.as_view(), name='api_transfer_coins'),
    path('burn-coins/', BurnCoinsView.as_view(), name='burn-coins'),
    path('api/transaction-history/', TransactionHistoryView.as_view(), name='transaction-history'),
]
