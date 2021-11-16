from django.db import models

class Tip(models.Model):
    """
    Representa un consejo de la base de datos
    """
    name = models.CharField(max_length=60)
    description = models.TextField(null=True)
    metadata = models.JSONField(null=True)
 
    class Meta:
        managed = True
        db_table = 'tips'

    def __str__(self):
        return self.name
