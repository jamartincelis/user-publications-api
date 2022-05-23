from uuid import uuid4

from django.db import models


class Catalog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    catalog_name = models.CharField(max_length=40)
    description = models.CharField(max_length=80)

    class Meta:
        db_table = 'catalogs'
        managed = True


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name='items')
    item_name = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    metadata = models.JSONField()
    active = models.BooleanField(default=True)
    process_name = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'items'
        managed = True
