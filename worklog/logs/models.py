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
    
class HealthType(Timestampable):
    name = models.CharField(max_length=250)
    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class Exercise(Timestampable):
    name = models.CharField()
    description = models.TextField()
    
    def __str__(self):
        return self.name    
    
# I could have added this to the above log but I created a seperate as I think this is far different then the normal log
class HealthLog(Timestampable):
    description = models.TextField()
    healthtype = models.ForeignKey(HealthType,on_delete=models.DO_NOTHING)
    # this time spent I will hope this is a float value
    time_spent = models.IntegerField(default=0)
    calorie = models.IntegerField(default=0)
    operation = models.SmallIntegerField(default=0)
    exercise_type = models.ForeignKey(Exercise,on_delete=models.DO_NOTHING)
    reps = models.IntegerField(default=0)
    
    def __str__(self):
        return self.description + ' : ' + str(self.time_spent) + ' : ' + self.created_at.strftime("%d/%m/%Y")
    
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