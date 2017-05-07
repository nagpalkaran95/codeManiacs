from django.shortcuts import render
from forums.models import Forum,Answer
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404,HttpResponseRedirect
from django.contrib.auth.models import User
from forums.models import Forum

# Create your views here.
def index(request):
    questions = Forum.objects.all()
    auth = request.user.is_authenticated()
    user = None
    flag = 0
    if auth:
        flag = 1
        user = User.objects.get(username = request.user.username)
        #username = request.user.username
    return render(request,'forums.html',{'questions': questions, 'flag': flag, 'user': user})

    

def thread(request, thread_id):
    try:
        question = Forum.objects.get(pk = thread_id)
    except ObjectDoesNotExist:
        question = None
    if question:
        answers = Answer.objects.filter(question__pk = thread_id)
        return render(request,'thread.html',{ 'question': question, 'answers': answers })
    else:
        raise Http404

def post(request):
    if request.method == "POST":
        question = request.POST.get("question", "")
        description = request.POST.get("description", "")
        author = request.user.username
        tags = request.POST.get("tags","")
        newQues = Forum(question = question, description = description, author = author, tags = tags)
        newQues.save()
        '''questions = Forum.objects.all()
        auth = request.user.is_authenticated()
        user = None
        flag = 0
        if auth:
            flag = 1
            user = User.objects.get(username = request.user.username)
        return render(request,'forums.html',{'questions': questions, 'flag': flag, 'user': user})
        '''
        return HttpResponseRedirect('/forums/')
    else:
        raise Http404