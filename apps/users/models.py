from django.db import models
TYPES = [
    ('admin', 'Admin'),
    ('user', 'User'),
    ('author', 'Author'),
]


class User(models.Model):
    username = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    user_type = models.CharField(max_length=50, choices=TYPES, default='user')
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.username