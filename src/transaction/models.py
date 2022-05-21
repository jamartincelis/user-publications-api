from uuid import uuid4

from django.db import models
from django.db.models.fields import UUIDField

from catalog.models import Item


class Transaction(models.Model):
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True)
    user_id = models.UUIDField(db_index=True, null=False)
    account_id = models.UUIDField(db_index=True, null=False)
    category_id = models.ForeignKey(Item, on_delete=models.DO_NOTHING, related_name='transaction_category')
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    description = models.CharField(max_length=100)
    transaction_date = models.DateTimeField()
    ignore_pfm = models.BooleanField(default=False)
    user_note = models.CharField(max_length=100, null=True, default=None, blank=True)
    created_at = models.DateTimeField(null=True, default=None)

    class Meta:
        db_table = 'transactions'
        managed = True
