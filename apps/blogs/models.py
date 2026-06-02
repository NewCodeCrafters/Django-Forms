from django.db import models
from django.utils.text import slugify
from apps.users.models import User

STATUS = (
    ("draft", "Draft"),
    ("published", "Published"),
    ("archived", "Archived"),
)

class Blogs(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    description = models.TextField()
    image = models.ImageField()
    status = models.CharField(max_length=20, choices=STATUS, default="draft")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)