"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.conf import settings  # Import settings to access MEDIA_URL and MEDIA_ROOT
from django.conf.urls.static import static  # Import static to help serve files
from homepage.views import index, impressum

urlpatterns = [
    path('admin/', admin.site.urls), # This is for the Admin Panel
    path('i18n/', include('django.conf.urls.i18n')), # This is for i18n
    path('', index, name='index'), # This is for the hoem page
    path('impressum/', impressum, name='impressum'), # This is for the ImpressumcPage

    path('robots.txt', RedirectView.as_view(url=static_file('robots.txt'), permanent=True)), # This safely routes /robots.txt to static/robots.txt file natively

    path("__reload__/", include("django_browser_reload.urls")), # This refreshes the page every time the code is changed.
]

# This serves media files only during development (when DEBUG = True)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)