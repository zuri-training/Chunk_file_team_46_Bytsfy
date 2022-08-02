from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True, default='profile_pics/img.png')
