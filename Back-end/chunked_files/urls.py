from django.urls import path
from .views import chunk

# app_name = "chunked_files"
urlpatterns = [
    path("chunk/", chunk, name="chunk"),
]