from django.shortcuts import render
from allauth.account.views import PasswordChangeView
from django.urls import reverse_lazy

# Create your views here.


class CustomPasswordChangeView(PasswordChangeView):
<<<<<<< HEAD
    success_url = reverse_lazy("password_change_done")
=======
    success_url = reverse_lazy("password_change_done") 


def signup(request):
    return render(request,"account/Signup.html")
>>>>>>> 26fe03046c8059a84b8472f2521b1353f0e09558
