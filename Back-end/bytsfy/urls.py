"""bytsfy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    # user authentication
<<<<<<< HEAD
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("allauth.urls")),  # new
=======
    path('accounts/', include('accounts.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),

    path('accounts/', include('allauth.urls')), # new
>>>>>>> 26fe03046c8059a84b8472f2521b1353f0e09558
    # social logins
    path("social-auth/", include("social_django.urls", namespace="social")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path("", TemplateView.as_view(template_name="dashboard.html"), name="dashboard"),
<<<<<<< HEAD
    path("chunked_files/", include("chunked_files.urls")),
=======

    path("", include('chunked_files.urls')),
>>>>>>> 26fe03046c8059a84b8472f2521b1353f0e09558
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
