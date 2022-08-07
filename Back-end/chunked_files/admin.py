from django.contrib import admin
from .models import Chunked, Uploaded_file

# Register your models here.
admin.site.register(Chunked)
admin.site.register(Uploaded_file)