from django.shortcuts import render, get_object_or_404, redirect
from .models import Blogs
from django.contrib import messages
from .forms import BlogForm
from apps.users.models import User
from apps.users.decorator import login_required

@login_required
def b_lists(request):

    blogs = Blogs.objects.filter(status="published").order_by("-created_at")

    context = {
        "blogs": blogs
    }

    return render(request, "blogs/b_list.html", context)

def details(request, slug):
    blog = get_object_or_404(
        Blogs,
        slug = slug
    )
    context = {
        "blog": blog
    }

    return render(request, "blogs/details.html", context)


@login_required
def post_blog(request, slug):
    if request.method == "POST":
        form = BlogForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            user = User.objects.get(id=request.session["user_id"])

            blog = form.save(commit = False)

            blog.author = user

            blog.save()

            messages.success(
                request,"Blog created successfully"
            )
            return redirect("details", slug=blog.slug)
        
        return render(request, "blogs/post.html", {"form": form})
            