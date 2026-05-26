from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "user_type", "created_at", "last_login" )
    search_fields = ("username", "email")
    list_filter = ("user_type",)

