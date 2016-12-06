#!python
#log/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import  UserCreationForm

#http://stackoverflow.com/questions/6288661/adding-a-user-to-a-group-in-django
from django.contrib.auth.models import Group

def home(request):
    """
    Home is the root of our test app for displaying the Django Source Control app
    """
    return render(request,"home/home_home.html")

def register(request):
    """
    Register uses a stock django form for creating new users the UserCreationForm 
    """
    template_name = "home/register.html"
    form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        try:
            group = Group.objects.get(name='Basic User')
            user.groups.add(group)
            user.save()
        except: 
            pass

        return render(request, "home/register_complete.html")
    return render(request, template_name, {'form': form})#, context)