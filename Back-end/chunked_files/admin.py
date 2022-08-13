from django.contrib import admin
from .models import Chunked, Contact, Subscribers

# Register your models here.
admin.site.register(Chunked)
admin.site.register(Contact)
admin.site.register(Subscribers)
