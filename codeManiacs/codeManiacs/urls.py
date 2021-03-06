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
from codeManiacs import views as codeManiacs_views
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', codeManiacs_views.index),
    url(r'^signUp/',codeManiacs_views.signUp),
    url(r'^login/',codeManiacs_views.logIn),
    url(r'^logout/',codeManiacs_views.logoutActiveUser),
    #url(r'^profile/(?P<user_id>\w+)/$',codeManiacs_views.profile),
    url(r'^profile/',include('users.urls')),
    url(r'^problems/',include('problems.urls')),
    #url(r'^about/', TemplateView.as_view(template_name = 'about.html')),
    url(r'^admin/', admin.site.urls),
    url(r'^forums/',include('forums.urls')),
]