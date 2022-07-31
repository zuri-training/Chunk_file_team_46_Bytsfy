from django.urls import path
from .views import signUp, LoginView

urlpatterns = [
    path("signup/", signUp, name="signup"),
    path("login/", LoginView.as_view(redirect_authenticated_user=True), name="login"),
]


# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']