import email
from typing_extensions import Required
from unittest.mock import DEFAULT
from django.db import models
from django.core.validators import EmailValidator


# Create your models here.

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