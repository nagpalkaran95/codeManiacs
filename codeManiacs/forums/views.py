from django.shortcuts import render
from forums.models import Forum,Answer
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404

# Create your views here.
def index(request):
    questions = Forum.objects.all()
    return render(request,'forums.html',{'questions': questions})

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