from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Identity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='identity/', blank=True, null=True, default='image/default_pilot_pfp.jpg')
    status = models.CharField(max_length=255, blank=True, default='No Status Yet')
