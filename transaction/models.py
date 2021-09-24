import uuid

from django.db import models
from django.db.models.fields import UUIDField

from catalog.models import Code

from account.models import Account

class Transaction(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Code, models.DO_NOTHING, null=True, default=None)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    description = models.CharField(max_length=100)
    transaction_date = models.DateTimeField()
    user_note = models.CharField(max_length=100, null=True, default=None)
    
    class Meta:
        managed = True
        db_table = 'transactions'
