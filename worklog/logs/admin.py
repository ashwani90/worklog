from django.contrib import admin

# Register your models here.
from .models import Category,Type,Log,Note,Post

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
    pass
    # list_display = ["description", "type"]
    

admin.site.register(Type, TypeAdmin)
admin.site.register(Log, LogAdmin)
admin.site.site_header = "Work Log"
admin.site.site_title = "Work Log"
admin.site.index_title = "Work Log"

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post

    list_display = (
        "id",
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )
    list_filter = (
        "published",
        "publish_date",
    )
    list_editable = (
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )
    search_fields = (
        "title",
        "subtitle",
        "slug",
        "body",
    )
    prepopulated_fields = {
        "slug": (
            "title",
            "subtitle",
        )
    }
    date_hierarchy = "publish_date"
    save_on_top = True