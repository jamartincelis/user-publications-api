from django.db import models


class Notification(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField()
    metadata = models.JSONField(null=True)
 
    class Meta:
        db_table = 'notifications'
        managed = True
