from django.db import models

class Notification(models.Model):
    """
    Representa una notificacion de la base de datos
    """
    description = models.TextField(null=True)
    metadata = models.JSONField(null=True)
 
    class Meta:
        managed = True
        db_table = 'notifications'

    def __str__(self):
        return self.name
