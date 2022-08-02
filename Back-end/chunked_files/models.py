from django.db import models
from accounts.models import User

# Create your models here.

class Chunked(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    zipped_file = models.FileField(upload_to="chunked_folder", blank= True)
    
