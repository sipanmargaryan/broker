from django.db import models, transaction


class AbstractDateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Wallet(AbstractDateModel):
    id = models.AutoField(primary_key=True)
    label = models.CharField(max_length=255)
    balance = models.DecimalField(max_digits=18, decimal_places=2, default=0)
    

class Transaction(AbstractDateModel):
    id = models.AutoField(primary_key=True)
    txid = models.CharField(max_length=255, unique=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2)

    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        with transaction.atomic():
            self.wallet.balance = self.wallet.balance + self.amount
            self.wallet.save()
            super().save(*args, **kwargs)