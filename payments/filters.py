from django_filters import rest_framework as filters

from payments.models import Transaction, Wallet



class TransactionFilter(filters.FilterSet):
    query = filters.CharFilter(method='filter_transaction_id')
    amount_min = filters.NumberFilter(field_name='amount', lookup_expr='gte')
    amount_max = filters.NumberFilter(field_name='amount', lookup_expr='lte')


    class Meta:
        model = Transaction
        fields = ["query"]

    @staticmethod
    def filter_transaction_id(queryset, name, value):
        if not value:
            return queryset

        return queryset.filter(txid__icontains=value)
    
    

class WalletFilter(filters.FilterSet):
    label = filters.CharFilter(method='filter_label')
    balance_min = filters.NumberFilter(field_name='balance', lookup_expr='gte')
    balance_max = filters.NumberFilter(field_name='balance', lookup_expr='lte')

    class Meta:
        model = Wallet
        fields = ["label", "balance", "balance"]

    @staticmethod
    def filter_label(queryset, name, value):
        if not value:
            return queryset

        return queryset.filter(label__icontains=value)
