from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm
from django.contrib.auth import views as auth_views
from .forms import LoginForm

# Create your views here.
# render image


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'
   

def signUp(request):
    # Prevent logged in user from accessing signup page
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    context = {"form": form}
    return render(request, "registration/signup.html", context)
    

