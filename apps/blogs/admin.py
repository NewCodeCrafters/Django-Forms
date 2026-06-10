from django.contrib import admin
from .models import Blogs, Question, Vote

@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "created_at", "updated_at")
    search_fields = ("title", "author__username")
    list_filter = ("status", "created_at")


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "votes", "created_at", "slug")
    search_fields = ("title", "author__username")
    list_filter = ("status", "created_at")

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ("user", "question", "created_at")
    search_fields = ("user__username", "question__title")
    list_filter = ("created_at",)
