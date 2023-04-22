from django.contrib import admin

# Register your models here.
from .models import Category,Type,Log,Note

admin.site.register(Category)
admin.site.register(Note)

@admin.action(description="Mark as completed")
def make_completed(modeladmin, request, queryset):
    queryset.update(completed=True)
    
# class LogInline(admin.TabularInline):
#     model = Log
    
class TypeAdmin(admin.ModelAdmin):
    list_display = ["name", "completed"]
    ordering = ["name"]
    actions = [make_completed]
    # inlines = [
    #     LogInline
    # ]
    
class LogAdmin(admin.ModelAdmin):
    list_display = ["description", "type"]
    

admin.site.register(Type, TypeAdmin)
admin.site.register(Log, LogAdmin)
admin.site.site_header = "Work Log"
admin.site.site_title = "Work Log"
admin.site.index_title = "Work Log"