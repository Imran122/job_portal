from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request, 'jobs/index.html')
@login_required(login_url='/login/')
def createJob(request):
    return render(request, 'jobs/createJob.html')
@login_required(login_url='/login/')
def jobList(request):
    return render(request, 'jobs/jobList.html')