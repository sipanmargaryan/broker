import pytest
import factory
from decimal import Decimal
from django.urls import reverse

from payments.factories import TransactionFactory, WalletFactory


@pytest.mark.django_db
def test_wallets_count(client):

    WalletFactory.create_batch(20)
    response = client.get(reverse('payments:wallets'))
    assert response.status_code == 200
    response = response.json()
    assert len(response["results"]) == 10


@pytest.mark.django_db
def test_wallets_filter_by_label(client):

    WalletFactory(label="bitcoin")
    WalletFactory(label="etherium")
    WalletFactory(label="arbitrum")
    response = client.get(reverse('payments:wallets'), data={"label": "arb"})
    assert response.status_code == 200
    response = response.json()
    assert len(response["results"]) == 1


@pytest.mark.django_db
def test_wallets_ordering(client):

    WalletFactory(label="bitcoin")
    WalletFactory(label="etherium")
    WalletFactory(label="arbitrum")
    response = client.get(reverse('payments:wallets'), data={"ordering": "label"})
    assert response.status_code == 200
    response = response.json()
    assert response["results"][0]["label"] == "arbitrum"
    assert response["results"][2]["label"] == "etherium"


@pytest.mark.django_db
def test_wallet_balance(client):
    wallet = WalletFactory(label="test")
    amounts = [10, 20.25, 14.50]
    transactions = TransactionFactory.create_batch(len(amounts), amount=factory.Iterator(amounts), wallet=wallet)
    response = client.get(reverse('payments:wallets'), data={"label": "test"})
    assert response.status_code == 200
    response = response.json()["results"][0]
    assert Decimal(response["balance"]) == Decimal(sum(amounts))


# To be continued