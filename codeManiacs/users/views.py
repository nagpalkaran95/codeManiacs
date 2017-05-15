from django.shortcuts import render
from django.contrib.auth.models import User
from users.models import UserProfile
# Create your views here.

def profile(request,user_id):
    #user = User.objects.get(username = user_id)
    user = User.objects.get(id = user_id)
    return render(request, 'profile.html', {'user' : user})
