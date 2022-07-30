from django.urls import path

from . import views


urlpatterns=[
    path("bytsfy",views.home)
]

