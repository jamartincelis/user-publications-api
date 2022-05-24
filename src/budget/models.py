from uuid import uuid4

from django.db import models

from catalog.models import Item


class Budget(models.Model):
    id = models.UUIDField(default=uuid4, unique=True, primary_key=True)
    user_id = models.UUIDField(db_index=True, null=False)
    category = models.ForeignKey(Item, on_delete=models.DO_NOTHING, related_name='budget_category')
    status = models.ForeignKey(Item, on_delete=models.DO_NOTHING, related_name='budget_status')
    amount = models.DecimalField(decimal_places=2, max_digits=12, default=0.0)
    budget_date = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'budgets'
