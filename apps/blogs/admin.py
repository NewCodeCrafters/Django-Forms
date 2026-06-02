from django.contrib import admin
from .models import Blogs

@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "created_at", "updated_at")
    search_fields = ("title", "author__username")
    list_filter = ("status", "created_at")

    
