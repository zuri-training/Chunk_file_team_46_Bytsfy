from django.urls import path
from .views import CustomPasswordChangeView
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path("password/change/", CustomPasswordChangeView.as_view(), name="account_password_change"), #new
    path("password/change/done", TemplateView.as_view(template_name="account/password_change_done.html"), name="password_change_done"),
    path("signup", views.signup)
]
