from django.shortcuts import render
from django.contrib.auth import logout,authenticate,login
from django.http import HttpResponseRedirect
from .forms import LogIn
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    return render(request, 'index.html')

def logIn(request):
    if request.method == "POST":
        handle = request.POST.get("handle",None)
        password = request.POST.get("password",None)
        user = authenticate(username=handle, password=password)
        if user is not None:
            login(request,user)
            return render(request, 'index.html',{'user' : user})
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')
    
def signUp(request):
    if request.method == "POST":
        handle = request.POST.get("handle",None)
        email = request.POST.get("email",None)
        password = request.POST.get("password",None)
        if not (User.objects.filter(username=handle).exists() or User.objects.filter(email=email).exists()):
            User.objects.create_user(handle, email, password)
            user = authenticate(username = handle, password = password)
            if user is not None:
                login(request,user)
                return render(request, 'index.html',{'user' : user})
            else:
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

def logoutActiveUser(request):
    logout(request)
    return HttpResponseRedirect('/')