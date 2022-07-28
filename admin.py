from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import CustomUser
from . import models
from . import forms


# Register your models here.
@admin.register(models.CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = forms.CustomUserCreationForm
    form = forms.CustomUserChangeForm
    model = models.CustomUser

    ordering = ["email"]
    list_display = ["email", "is_staff", "is_active", "is_superuser"]
    search_fields = ["email"]

    fieldsets = (
        (None, {
            "fields": (
                'email', 'password'
            ),
        }),
        ('Details', {
            "fields": (
                'fullname',
            ),
        }),
        ('Permissions', {
            "fields": (
                'is_staff', 'is_active'
            ),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'fullname', 'password1', 'password2'),
        }),
    )