"""codeManiacs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from forums import views as forums_views
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$',forums_views.index),
    url(r'^thread/(?P<thread_id>\d+)/$',forums_views.thread),
    url(r'^threadpost/$',forums_views.post),
    #url(r'^(?P<user_id>.+)/$',users_views.profile),
]