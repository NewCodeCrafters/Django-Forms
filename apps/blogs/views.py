from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from .models import Blogs
from .forms import BlogForm
from apps.users.models import User
from apps.users.decorator import login_required


@login_required
def b_lists(request):
    blogs = Blogs.objects.filter(status="published").order_by("-created_at")
    return render(request, "blogs/b_list.html", {"blogs": blogs})


@login_required
def details(request, slug):
    blog = get_object_or_404(Blogs, slug=slug)
    return render(request, "blogs/details.html", {"blog": blog})


@login_required
def post_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)

        if form.is_valid():
            user = User.objects.get(id=request.session["user_id"])
            blog = form.save(commit=False)
            blog.author = user
            blog.save()
            messages.success(request, "Blog created successfully")
            return redirect("details", slug=blog.slug)


        return render(request, "blogs/post.html", {"form": form})

    form = BlogForm()
    return render(request, "blogs/post.html", {"form": form})


@login_required
def update(request, slug):
    user = User.objects.get(id=request.session["user_id"])
    blog = get_object_or_404(Blogs, slug=slug, author=user)

    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)

        if form.is_valid():
            form.save()
            messages.success(request, "Blog updated successfully")
            return redirect("details", slug=blog.slug)

    else:
        form = BlogForm(instance=blog)      
    return render(request, "blogs/update.html", {"form": form, "blog": blog})


@login_required
def delete(request, slug):
    user = User.objects.get(id=request.session["user_id"])
    blog = get_object_or_404(Blogs, slug=slug, author=user)

    if request.method == "POST":
        blog.delete()
        messages.success(request, "Blog deleted successfully")
        return redirect("b_list")           

    return render(request, "blogs/delete.html", {"blog": blog})