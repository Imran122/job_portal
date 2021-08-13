from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('createJob/', views.createJob, name = 'createJob'),
	path('jobList/', views.jobList, name = 'jobList'),
	path('jobDetails/<slug:slug>', views.jobDetails, name ='jobDetails'),
	path('applyJob/<int:job_id>/', views.applyJob, name ='applyJob'),
	

]
