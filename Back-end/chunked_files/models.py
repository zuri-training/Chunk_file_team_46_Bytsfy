from django.db import models
from accounts.models import User


import email
from typing_extensions import Required
from unittest.mock import DEFAULT

# Create your models here.

class Chunked(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    zipped_file = models.FileField(upload_to="chunked_folder", blank= True)


class UploadedFile(models.Model):
    uploaded_file = models.FileField(upload_to="uploaded")


# new_eric

SUBJECT_CHOICES= ( ('Choose a subject','Choose a subject'),
                  ('General Info','General Info'), 
                  ('Suggest a Feature','Suggest a Feature'),
                  ('Report a Problem','Report a Problem'),
                  ('Privacy','Privacy'),)


class Contact(models.Model):
    email=models.EmailField(max_length=200)
    subject = models.CharField(max_length = 50,choices = SUBJECT_CHOICES)
    message=models.TextField(max_length = 255)

# DEFAULT= 'General Info'

    def __str__(self):
        return f"{self.email} ({self.subject}) ({self.message})"


class Subscribers(models.Model):
     subscribers_email=models.EmailField(max_length=200)
     
     def __str__(self):
      return self.subscribers_email