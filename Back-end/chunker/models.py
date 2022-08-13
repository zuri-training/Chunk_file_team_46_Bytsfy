from django.db import models
from accounts.models import User
# from cloudinary_storage.storage import RawMediaCloudinaryStorage

# Create your models here.


class OurUser(User):
    pass

class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    file_name = models.CharField(max_length=500, blank=True)
    uploaded_file = models.FileField()
    zip_file = models.FileField()
    saved_file = models.FileField()
    saved_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name
        