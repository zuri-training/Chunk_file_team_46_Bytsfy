from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .managers import CustomUserManager


# Create your models here.

class CustomUser(AbstractUser, PermissionsMixin):
    username = None
    last_name = None
    first_name = None
    email = models.EmailField(unique=True)
    fullname = models.CharField(max_length=20)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        ordering = ['email']
        verbose_name = 'User'

    def __str__(self):
        return self.email

    # Create your models here.
