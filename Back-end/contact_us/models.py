import email
from typing_extensions import Required
from unittest.mock import DEFAULT
from django.db import models

# Create your models here.

SUBJECT_CHOICES= (('General Info','General Info'), 
                  ('Suggest a Feature','Suggest a Feature'),
                  ('Report a Problem','Report a Problem'),
                  ('Privacy','Privacy'),)



class Contact(models.Model):
    email=models.EmailField(max_length=100)
    subject = models.CharField(max_length = 50,choices = SUBJECT_CHOICES)
    message=models.TextField(max_length = 255)

# DEFAULT= 'General Info'