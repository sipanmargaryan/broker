import factory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyDecimal

from payments.models import Wallet, Transaction

class WalletFactory(DjangoModelFactory):
    class Meta:
        model = Wallet

    label = factory.Faker('word')

class TransactionFactory(DjangoModelFactory):
    class Meta:
        model = Transaction

    txid = factory.Faker('uuid4')
    amount = FuzzyDecimal(1, 100, 8)  

    wallet = factory.SubFactory(WalletFactory)