from django.db import models
from django.utils.text import slugify

from apps.users.models import User
STATUS = (
        ("active", "Active"),
        ("closed", "Closed"),
    )


class Question(models.Model):
    
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name="questions")
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    status = models.CharField(max_length=20,choices=STATUS,default="active")
    votes = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Vote(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name="question_votes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "question")

    def save(self, *args, **kwargs):
        is_new = self.pk is None

        super().save(*args, **kwargs)

        if is_new:
            self.question.votes += 1
            self.question.save()

    def __str__(self):
        return f"{self.user} voted for {self.question}"