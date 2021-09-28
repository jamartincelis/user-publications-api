import uuid

from django.db import models
from django.db.models.fields import UUIDField

from catalog.models import Code

from user.models import User


class Budget(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, related_name='budgets')
    category = models.ForeignKey(Code, models.DO_NOTHING)
    amount = models.DecimalField(decimal_places=2, max_digits=12)
    expenses_sum = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    expenses_count = models.SmallIntegerField(default=0)
    average = models.DecimalField(decimal_places=2, max_digits=12, default=0)
    spent = models.DecimalField(decimal_places=1, max_digits=3, default=0)
    budget_date = models.DateField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'budgets'
