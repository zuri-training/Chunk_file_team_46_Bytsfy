from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.


class User(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, default='profile_pics/avatar.svg')
    country = models.CharField(max_length=250, null=True)
    phone = models.CharField(max_length=20, null=True)

