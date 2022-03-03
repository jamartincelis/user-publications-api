import uuid

from django.db import models
from django.db.models.fields import UUIDField

class Transaction(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    account = models.UUIDField(db_index=True, null=False)
    user = models.UUIDField(db_index=True, null=False)
    category = models.UUIDField(db_index=True, null=False)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    description = models.CharField(max_length=100)
    transaction_date = models.DateTimeField()
    user_note = models.CharField(max_length=100, null=True, default=None, blank=True)
    
    class Meta:
        managed = True
        db_table = 'transactions'


class MonthlySummary(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    user = models.UUIDField(db_index=True, null=False)
    incomes_sum = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    incomes_count = models.SmallIntegerField(default=0)
    expenses_sum = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    expenses_count = models.SmallIntegerField(default=0)
    balance = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    summary_date = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'monthly_summaries'