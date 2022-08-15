from django.shortcuts import render, redirect
from allauth.account.views import PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Create your views here.

# creating a password change success view
@login_required(login_url="account_login")
def homePage(request):
    return render(request, "HomePage.html")


def landingPage(request):
    if request.user.is_authenticated:
        return redirect("home-page")
    return render(request, "landing_page.html")


@login_required(login_url="account_login")
def profilePage(request):
    return render(request, "PersonalDetails.html")


@login_required(login_url="account_login")
def updateProfile(request):
    return render(request, "profile.html")

class CustomPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy("password_change_done")


# password_reset = PasswordResetView.as_view()


# class PasswordResetDoneView(TemplateView):
#     template_name = "account/password_reset_done."