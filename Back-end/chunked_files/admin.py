from django.contrib import admin
from .models import Chunked, UploadedFile, Contact, Subscribers

# Register your models here.

admin.site.register(UploadedFile)

# Register your models here.
admin.site.register(Chunked)
admin.site.register(Contact)
admin.site.register(Subscribers)
