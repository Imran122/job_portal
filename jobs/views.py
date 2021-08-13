from django.http.response import HttpResponse
from jobs.models import Categorey, Job, JobApplication, User
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import JobApplicationForm
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request, 'jobs/index.html')


@login_required(login_url='/login/')
def createJob(request):
    categories = Categorey.objects.all()
    
    if request.method == 'POST':
        print("success,.,.,.,.,#@@@@")
        title= request.POST['title']
        categories= request.POST['categories']
        companyName= request.POST['companyName']
        address= request.POST['address']
        experience= request.POST['experience']
        salary= request.POST['salary']
        vacancy= request.POST['vacancy']
        employmentStatus= request.POST['employmentStatus']
        jobResponsibilities= request.POST['jobResponsibilities']
        additionalRequirements= request.POST['additionalRequirements']
        benefits = request.POST['benefits']
        jobContext = request.POST['jobContext']
        expiredate = request.POST['expiredate']
        category_obj = Categorey.objects.get(title=categories)   
        print("in form save.,xx.,.,#@@@@")
        temp = Job(title=title,categories=category_obj,companyName=companyName,address=address,experience=experience,salary=salary,vacancy=vacancy,employmentStatus=employmentStatus,jobResponsibilities=jobResponsibilities,additionalRequirements=additionalRequirements,benefits=benefits,expiredate=expiredate,jobContext=jobContext,)
           
        temp.save()
        messages.success(request, 'You are messages submitted')
        print("success,.,.,.,.,#@@@@")
        return render(request, 'jobs/createJob.html') 
    context ={
       
        "categories": categories,
    }
    return render(request, 'jobs/createJob.html',context)




def jobList(request):
    job_list = Job.objects.all()
    context = {
        'job_list': job_list,
    }
    return render(request, 'jobs/jobList.html',context)


def jobDetails(request, slug):
    job = Job.objects.filter(slug=slug)
    
    if job.exists():
        job = job.first()
    else:
        HttpResponse("<h3>page not found</h3>")
    context ={
        'job':job,
    }
    return render(request, 'jobs/jobDetails.html',context)


#apply job view     
def applyJob(request, job_id):
    job = Job.objects.get(pk=job_id)
    user = request.user
    if request.method == 'POST':
        print("xxxxxx.....1..")
        form = JobApplicationForm(request.POST, request.FILES)
        print("xxxxxx......2.")
        if form.is_valid():
            print("xxxxxx.....3..")
            application = form.save(commit=False)
            application.job =job
            application.user = request.user
            application.save()
            return render(request, 'jobs/applyJob.html') 
    else:
        form = JobApplicationForm()
    return render(request, 'jobs/applyJob.html',{'form':form,'job':job,})