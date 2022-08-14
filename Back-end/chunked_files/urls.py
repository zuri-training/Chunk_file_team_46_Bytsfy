from django.urls import path
from .views import chunk
from . import views


# app_name = "chunked_files"
urlpatterns = [
    path("", chunk, name="chunk"),
]