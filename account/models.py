import uuid

from django.db import models

from user.models import User


class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, models.DO_NOTHING, related_name='accounts')

    class Meta:
        managed = True
        db_table = 'accounts'

    def __str__(self):
        return str(self.id)
