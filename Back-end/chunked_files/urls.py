from string import Template
from django.urls import path
from .views import chunk
from django.views.generic import TemplateView

app_name = "chunked_files"
urlpatterns = [
    path("", chunk, name="chunk"),
    
]
