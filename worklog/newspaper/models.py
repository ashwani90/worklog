from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import pre_save
from datetime import datetime

# Create your models here.

class Timestampable(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
    class Meta:
        abstract = True
        ordering = ['-created_at']
    
class NewspaperContent(Timestampable):
    page_num = models.IntegerField(default=0)
    vlocation = models.IntegerField(default=0)
    hlocation = models.IntegerField(default=0)
    heading = models.CharField(default='',max_length=2000)
    description = models.TextField(default='')
    date = models.DateField(auto_now=True)
    by = models.CharField(default='',max_length=500)
    from_ref = models.CharField(default='',max_length=500)
    
class News(Timestampable):
    new_head = models.CharField(default='', max_length=2000)
    description = models.TextField()
    source = models.CharField(max_length=500)
    
    @receiver(pre_save)
    def set_dates(sender, instance, **kwargs):
        instance.created_at = datetime.now()
        instance.updated_at = datetime.now()
        