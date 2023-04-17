from django.contrib import admin

# Register your models here.
from .models import Category,Type,Log

admin.site.register(Category)
admin.site.register(Type)
admin.site.register(Log)