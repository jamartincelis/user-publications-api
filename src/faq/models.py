from django.db import models

class Faq(models.Model):
    
    question         = models.CharField(max_length=200, blank=True, null=True)
    answer           = models.TextField(blank=True, null=True)
    
    class Meta:
        managed = True
        db_table = 'faqs'