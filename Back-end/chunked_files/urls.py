from django.urls import path
from .views import chunk
from . import views


# app_name = "chunked_files"
urlpatterns = [
    path("chunk/", chunk, name="chunk"),
    path("contact/", views.contact, name ="contact"),
    path("thank-you/", views.thank_you),
]