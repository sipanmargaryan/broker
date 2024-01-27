from django.contrib import admin

from payments.models import Transaction, Wallet

admin.site.register(Transaction)
admin.site.register(Wallet)