from django.shortcuts import render
from django.contrib.auth import logout,authenticate,login
from django.http import HttpResponseRedirect
from .forms import LogIn
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from forums.models import Forum

def index(request):
    auth = request.user.is_authenticated()
    user = None
    if auth:
        user = User.objects.get(username = request.user.username)
    posts = Forum.objects.all().order_by('-dateCreated')
    return render(request, 'index.html', {'user': user,'posts': posts})

def logIn(request):
    if request.method == "POST":
        handle = request.POST.get("handle",None)
        password = request.POST.get("password",None)
        user = authenticate(username=handle, password=password)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/')
            #return render(request, 'index.html',{'user' : user})
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
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')

def logoutActiveUser(request):
    logout(request)
    return HttpResponseRedirect('/')
