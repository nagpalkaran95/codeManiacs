from django.shortcuts import render
from problems.models import ProblemSet

# Create your views here.
def problemIndex(request):
    problems = ProblemSet.objects.all()
    badgeCount = {}
    for i in problems:
        tags = i.tags.split()
        for j in tags:
            if j in badgeCount:
                badgeCount[j] += 1
            else:
                badgeCount[j] = 1
    return render(request, 'problems.html' , {'problems': problems, 'badgeCount': badgeCount} )

def problemWithID(request,problemID):
    try:
        problem = ProblemSet.objects.get(pk = problemID)
        return render(request, 'problemPage.html', {'problem': problem})
    except:
        return render(request, 'index.html')

def problemSubmit(request,problemID):
    return render(request,'submit.html')