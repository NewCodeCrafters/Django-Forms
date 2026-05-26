from django.shortcuts import render, get_object_or_404
from .models import Blogs

def blog_list(request):
    blogs = Blogs.objects.filter(status="Approved")
    context = {
        "blogs": blogs
    }
    return render(request, "blogs_list.html", context)

def blog_detail(request, slug):
    # blog =Blogs.objects.get(slug=slug)
    blog = get_object_or_404(Blogs, slug=slug)

    context = {
        "blog": blog
    }

    return render(request, "detail.html", context)
