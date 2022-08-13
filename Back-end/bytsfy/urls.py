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

    path("accounts/", include("accounts.urls")),
    path("accounts/", include("allauth.urls")),

    # social logins
    path("social-auth/", include("social_django.urls", namespace="social")),
    path("", TemplateView.as_view(template_name="base.html"), name="home"),
    path("", TemplateView.as_view(template_name="dashboard.html"), name="dashboard"),
    path("FAQ", TemplateView.as_view(template_name="FAQ.html"), name="FAQ"),
    path("Blog", TemplateView.as_view(template_name="blog.html"), name="Blog"),
    # path("contact", TemplateView.as_view(template_name="contact.html"), name="contact"),     #included in chunked_files app
    path("upload", TemplateView.as_view(template_name="upload.html"), name="upload"),
    path("getStarted", TemplateView.as_view(template_name="getStarted.html"), name="about"),
    path("chunk/", include("chunked_files.urls")),
    path("", include('chunker.urls')),
    path("",include('chunked_files.urls'))

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
