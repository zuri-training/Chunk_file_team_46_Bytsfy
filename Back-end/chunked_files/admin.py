from django.contrib import admin
from .models import Chunked, UploadedFile

# Register your models here.
admin.site.register(Chunked)
admin.site.register(UploadedFile)