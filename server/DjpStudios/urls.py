"""DjpStudios URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views

#You any login form can be used
from home.forms import LoginForm

urlpatterns = [
    url(r'^', include('home.urls')),

    #Home contains the base page and the register user page
    url(r'^home/', include('home.urls')),
    #The admin site is a place to manage all of the apps installed on our server.
    url(r'^admin/', admin.site.urls), 

    #Login / Logout mechanic for the server
    url(r'^login/$', auth_views.login, {'template_name': 'login.html', 'authentication_form': LoginForm}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}),

    #Django Source Control 
    url(r'^djangosourcecontrol/', include('djangosourcecontrol.urls')),
]
