import uuid

from django.db import models
from django.db.models.fields import UUIDField
from uuid import uuid4

class Budget(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    user = models.UUIDField(db_index=True, null=False)
    category = models.UUIDField(db_index=True, null=False)
    amount = models.DecimalField(decimal_places=2, max_digits=12, default=0.0)
    budget_date = models.DateField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'budgets'