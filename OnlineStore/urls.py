"""OnlineStore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
#from rest_framework.urlpatterns import format_suffix_patterns
from main import views
from django.conf import settings
from django.contrib.staticfiles import views as views_files

from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {})

def content_home(request):
    return render(request, 'content_home.html', {})

def details_products(request):
    return render(request, 'details_products.html', {})


urlpatterns = [
    url(r'^admin/', admin.site.urls),
   	url(r'^home/', index),
    url(r'^content_home', content_home),
    url(r'^details_products', details_products),

   	url(r'^about/', views.about),
    url(r'^add-products/', views.add_products),
    url(r'^details-products/', views.details_products),
   	url(r'^sign_up/', views.sign_up),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('', include('api_rest.urls', namespace='api_rest')),
    #url(r'^static/(?P<path>.*)$', views_files.serve),
] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



