from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AuthenticationForm
from .models import User
from django.utils.translation import gettext_lazy as _



class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email or Username')
    error_messages = {
        'invalid_login': _(
            "Username or Password incorrect."
            "fields may be case-sensitive."
        ),
        'inactive': _("This account is inactive."),
    }
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", ]
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        # To remove auto-focus in username input
        self.fields['username'].widget.attrs.update({'autofocus': False})
        # To remove help-text in the form
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
        



class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "username", "profile_pic"]
class CustomUserProfilePic(UserCreationForm):
    model = User
    fields = ["profile_pic"]
    def __init__(self, *args, **kwargs):
        self.fields['profile_pic'].widget = forms.FileInput()