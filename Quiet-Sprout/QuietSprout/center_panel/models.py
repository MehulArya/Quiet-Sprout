from django.db import models
from django.contrib.auth.models import User

#Create your models here.

class MidnightLogs(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_log')
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default='thoughts')
    content = models.TextField()
    created_timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} by {self.author.username}"
