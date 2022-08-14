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
from chunked_files.views import contact
from accounts.views import homePage, landingPage, profilePage


urlpatterns = [
    path("admin/", admin.site.urls),
    # user authentication

    path("accounts/", include("allauth.urls")),
    path("accounts/", include("accounts.urls")),
    path("chunker/", include("chunker.urls")),
    
    # social logins
    path("social-auth/", include("social_django.urls", namespace="social")),
<<<<<<< HEAD
=======
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
>>>>>>> main


    path("", landingPage, name="landing-page"),
    path("homepage.html", homePage, name="home-page"),
    path("profile.html", profilePage, name="profile-page"),
    path("FAQ.html", TemplateView.as_view(template_name="FAQ.html"), name="faq-page"),
    
    path("testimonial.html", TemplateView.as_view(template_name="testimonial.html"), name="testimonial-page"),
    path("documentation.html", TemplateView.as_view(template_name="API-introduction.html"), name="api-page"),
    path("documentation.html/get-started", TemplateView.as_view(template_name="getStarted.html"), name="api-getstarted"),
    path("contact.html", contact, name="contact-page"),

    # Blog page and its linked pages routing
    path("Blog.html", TemplateView.as_view(template_name="blog.html"), name="blog-page"),
    path("Blog.html/1", TemplateView.as_view(template_name="blogpg0.html"), name="blogpg0"),
    path("Blog.html/2", TemplateView.as_view(template_name="blogpg1.html"), name="blogpg1"),
    path("Blog.html/3", TemplateView.as_view(template_name="blogpg2.html"), name="blogpg2"),
    path("Blog.html/4", TemplateView.as_view(template_name="blogpg3.html"), name="blogpg3"),
    path("Blog.html/5", TemplateView.as_view(template_name="blogpg4.html"), name="blogpg4"),
    path("Blog.html/6", TemplateView.as_view(template_name="blogpg5.html"), name="blogpg5"),
    path("Blog.html/7", TemplateView.as_view(template_name="blogpg6.html"), name="blogpg6"),
    path("Blog.html/8", TemplateView.as_view(template_name="blogpg7.html"), name="blogpg7"),
    path("Blog.html/9", TemplateView.as_view(template_name="blogpg8.html"), name="blogpg8"),
    path("Blog.html/0", TemplateView.as_view(template_name="blogpg9.html"), name="blogpg9"),
    

     # Resource page and its linked pages routing
    path("resource.html", TemplateView.as_view(template_name="resourcemain.html"), name="resource-page"),
    path("resource.html/1", TemplateView.as_view(template_name="resourcepg1.html"), name="resourcepg1"),
    path("resource.html/2", TemplateView.as_view(template_name="resourcepg2.html"), name="resourcepg2"),
    path("resource.html/3", TemplateView.as_view(template_name="resourcepg3.html"), name="resourcepg3"),
    path("resource.html/4", TemplateView.as_view(template_name="resourcepg4.html"), name="resourcepg4"),
    path("resource.html/5", TemplateView.as_view(template_name="resourcepg5.html"), name="resourcepg5"),
    path("resource.html/6", TemplateView.as_view(template_name="resourcepg6.html"), name="resourcepg6"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
