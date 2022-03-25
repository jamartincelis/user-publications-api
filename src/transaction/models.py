from uuid import uuid4

from django.db import models
from django.db.models.fields import UUIDField


class Transaction(models.Model):
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True)
    account = models.UUIDField(db_index=True, null=False)
    user = models.UUIDField(db_index=True, null=False)
    category = models.UUIDField(db_index=True, null=True, default=None)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    description = models.CharField(max_length=100)
    transaction_date = models.DateTimeField()
    ignore_pfm = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True, default=None)

    class Meta:
        managed = True
        db_table = 'transactions'


class TransactionNote(models.Model):
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True)
    transaction = models.ForeignKey(Transaction, on_delete=models.DO_NOTHING)
    note = models.CharField(max_length=200)
    created_at = models.DateTimeField(null=True, default=None)

    class Meta:
        managed = True
        db_table = 'transaction_notes'


class UserClassifiedTransaction(models.Model):
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True)
    transaction = models.ForeignKey(Transaction, on_delete=models.DO_NOTHING)
    previous_category = models.UUIDField(null=False)
    current_category = models.UUIDField(null=False)
    created_at = models.DateTimeField(null=True, default=None)

    class Meta:
        managed = True
        db_table = 'user_classified_transactions'
