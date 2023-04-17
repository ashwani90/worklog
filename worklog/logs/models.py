from django.db import models

# Create your models here.

class Timestampable(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        abstract = True
    
class Category(Timestampable):
    name = models.CharField(max_length=250)
    description =  models.CharField()
    
    def __str__(self):
        return self.name
    
class Type(Timestampable):
    name = models.CharField(max_length=250)
    description = models.CharField()
    
    def __str__(self):
        return self.name

class Log(Timestampable):
    description = models.CharField()
    type = models.ForeignKey(Type,on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    time_spent = models.IntegerField()
    
    def __str__(self):
        return self.description
    

    
    