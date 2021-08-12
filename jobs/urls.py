from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('createJob/', views.createJob, name = 'createJob'),
	path('jobList/', views.jobList, name = 'jobList'),
	

]
