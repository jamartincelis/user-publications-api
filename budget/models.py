import uuid
from django.db.models.fields import UUIDField
from catalog.models import Code
from django.db import models
from user.models import User

class Budget(models.Model):
    id                  = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    budget_date         = models.DateTimeField()
    user                = models.ForeignKey(User, models.DO_NOTHING, blank=True, null=True)
    category            = models.ForeignKey(Code, models.DO_NOTHING, blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'budgets'
