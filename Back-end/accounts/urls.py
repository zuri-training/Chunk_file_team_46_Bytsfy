from django.urls import path
from . import views
from .views import CustomPasswordChangeView
from django.views.generic import TemplateView


urlpatterns = [

    #new
    # path("signup/", views.signup, name="account_signup"),
    # path("login/", views.login, name="account_login"),
    # path("logout/", views.logout, name="account_logout"),


    path("password/change/", CustomPasswordChangeView.as_view(), name="account_password_change"), #new
    path("password/change/done", TemplateView.as_view(template_name="account/password_change_done.html"), name="password_change_done"),
]
