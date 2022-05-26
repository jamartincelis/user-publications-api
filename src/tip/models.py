from django.db import models


class Tip(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(null=True)
    metadata = models.JSONField(null=True)
 
    class Meta:
        db_table = 'tips'
        managed = True
