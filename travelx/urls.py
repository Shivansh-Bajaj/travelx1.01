"""travelx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from bus import views
from cab import view
from view import main
urlpatterns = [
    url(r'^$',main,name='main'),
    #url(r'^/'),include('bus.url'),
    url(r'^bus$',views.index,name='busindex'),
    url(r'^search$',views.search,name='busearch'),
    url(r'^cab$',view.index,name='cabindex'),
    url(r'^cabsearch$',view.cab,name='cabsearch')
]
