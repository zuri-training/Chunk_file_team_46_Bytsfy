from string import Template
from django.urls import path
from .views import chunk
from django.views.generic import TemplateView

# app_name = "chunked_files"
urlpatterns = [
<<<<<<< HEAD
    path("", chunk, name="chunk"),
    
]
=======
    path("chunk/", chunk, name="chunk"),
]
>>>>>>> 26fe03046c8059a84b8472f2521b1353f0e09558
