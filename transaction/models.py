import uuid
from django.db.models.fields import UUIDField
from catalog.models import Code
from django.db import models
from user.models import User

class Transaction(models.Model):
    id                  = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    amount              = models.DecimalField(decimal_places=2, max_digits=30, blank=True, null=True)
    description         = models.CharField(max_length=100, blank=True, null=True)
    transaction_date    = models.DateTimeField()
    user                = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_transactions')
    category            = models.ForeignKey(Code, models.DO_NOTHING, blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'transactions'
