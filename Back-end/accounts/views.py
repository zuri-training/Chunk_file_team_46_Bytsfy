from django.shortcuts import render
from allauth.account.views import PasswordChangeView
from django.urls import reverse_lazy

# Create your views here.

# creating a password change success view
class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy("password_change_done")

