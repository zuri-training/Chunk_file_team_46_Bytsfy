from django.urls import path
from . import views
from .views import CustomPasswordChangeView
from django.views.generic import TemplateView


urlpatterns = [
    path("password/change/", CustomPasswordChangeView.as_view(), name="account_password_change"), #new
    path("password/change/done", TemplateView.as_view(template_name="account/password_change_done.html"), name="password_change_done"),
 ]
