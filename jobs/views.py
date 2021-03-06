from django.http.response import HttpResponse
from jobs.models import Categorey, Job, JobApplication, User
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import JobApplicationForm
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def index(request):
    return render(request, 'jobs/index.html')


@login_required(login_url='/login/')
def createJob(request):
    categories = Categorey.objects.all()
    
    if request.method == 'POST':
        
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
        #saving data in temp    
        temp.save()
        messages.success(request, 'You are messages submitted')
        #print("success,.,.,.,.,#@@@@")
        return render(request, 'jobs/createJob.html') 
    context ={
       
        "categories": categories,
    }
    return render(request, 'jobs/createJob.html',context)




def jobList(request):
    queryset = Job.objects.all()
    paginator = Paginator(queryset, 6)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        
        'queryset': queryset,
        'page_request_var': page_request_var,
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
@login_required(login_url='/login/')  
def applyJob(request, job_id):
    job = Job.objects.get(pk=job_id)
    user = request.user
    if request.method == 'POST':
        #print("xxxxxx.....1..")
        form = JobApplicationForm(request.POST, request.FILES)
       
        if form.is_valid():
            
            application = form.save(commit=False)
            application.job =job
            application.user = request.user
            application.save()
            messages.success(request, 'You are resume submitted')
            return render(request, 'jobs/applyJob.html')
        else:
            messages.error(request, 'ivalid submitted')
            return render(request, 'jobs/applyJob.html') 
    else:
        form = JobApplicationForm()
        
    return render(request, 'jobs/applyJob.html',{'form':form,'job':job,})