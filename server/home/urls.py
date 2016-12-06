#!python
# log/urls.py
from django.conf.urls import url
from . import views

app_name = 'home'
# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^register/$', views.register, name = 'register'),
]
