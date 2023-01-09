from django.shortcuts import render
from jobapp.models import JobPost,Location,Author,Skill


# Create your views here.
def job(request):
    jobAll = JobPost.objects.all()
    return render(request, 'jobapp/job.html', {'name':'job', 'jobAll':jobAll,})
def joblist(request,id=0):
    jobOne = JobPost.objects.get(id=id)
    return render(request, 'jobapp/joblist.html', {'name':'joblist','jobOne':jobOne,})
