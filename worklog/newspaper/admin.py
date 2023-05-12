from django.contrib import admin

from .models import NewspaperContent,News

# Register your models here.
admin.site.register(NewspaperContent)
admin.site.register(News)