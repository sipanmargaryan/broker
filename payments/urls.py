from django.urls import path

from payments.views import TransactionsAPIView, WalletAPIView

app_name = 'payments'
urlpatterns = [
    path('wallets', WalletAPIView.as_view(), name='wallets'),
    path('transactions', TransactionsAPIView.as_view(), name='transactions'),
]