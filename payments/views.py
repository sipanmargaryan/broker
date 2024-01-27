from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from payments.models import Transaction, Wallet
from payments.filters import WalletFilter, TransactionFilter
from payments.serializers import TransactionSerializer, WalletSerializer


class TransactionsAPIView(generics.ListAPIView):
    queryset = Transaction.objects.all().order_by('-id') 
    serializer_class = TransactionSerializer

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, )
    filterset_class = TransactionFilter
    ordering_fields = ["id", "amount", "created_at"]

class WalletAPIView(generics.ListAPIView):
    queryset = Wallet.objects.all().order_by('-id') 
    serializer_class = WalletSerializer

    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_class = WalletFilter
    ordering_fields = ["id", "balance", "label", "created_at"]