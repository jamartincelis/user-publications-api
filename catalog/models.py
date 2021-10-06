import uuid

from django.db import models


class CodeType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=100, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'codetypes'

    def __str__(self):
        return self.name


class Code(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=100, null=True, default=None)
    code_type = models.ForeignKey(CodeType, on_delete=models.CASCADE, related_name='codes')
    metadata = models.JSONField(default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'codes'

    def __str__(self):
        return self.name
