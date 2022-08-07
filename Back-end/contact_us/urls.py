from django.urls import path

from . import views

urlpatterns=[
    path("", views.ContactView.as_view()),
    path("subscription", views.SubscriberView.as_view()),
]