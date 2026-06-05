from django.urls import path
from . import views

urlpatterns = [
    path("list/",              views.b_lists,   name="b_list"),
    path("create/",            views.post_blog, name="post_blog"),   # no slug
    path("<slug:slug>/",       views.details,   name="details"),
    path("<slug:slug>/edit/",  views.update,    name="update"),
    path("<slug:slug>/delete/",views.delete,    name="delete"),
]