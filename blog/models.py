from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=3000)
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
