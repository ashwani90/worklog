from django.db import models
from django.conf import settings

# Create your models here.

class Timestampable(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    class Meta:
        abstract = True
        ordering = ['-created_at']
    
class Category(Timestampable):
    name = models.CharField(max_length=250)
    description =  models.TextField()
    
    def __str__(self):
        return self.name
    
class Type(Timestampable):
    name = models.CharField(max_length=250)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Log(Timestampable):
    description = models.TextField()
    type = models.ForeignKey(Type,on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    time_spent = models.IntegerField()
    
    def __str__(self):
        return self.description + ' : ' + str(self.time_spent) + ' : ' + self.created_at.strftime("%d/%m/%Y")
    
class Note(Timestampable):
    description = models.TextField()
    heading = models.CharField()
    
    def __str__(self):
        return self.heading
    
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    website = models.URLField(blank=True)
    bio = models.CharField(max_length=240,blank=True)
    
    def __str__(self):
        return self.user.get_username()
    
class Tag(models.Model):
    name = models.CharField(max_length=50,blank=True)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    class Meta:
        ordering = ["-publish_date"]

    title = models.CharField(max_length=255, unique=True)
    subtitle = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique=True)
    body = models.TextField()
    meta_description = models.CharField(max_length=150, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)

    author = models.ForeignKey(Profile, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)