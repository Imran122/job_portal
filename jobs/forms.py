from .models import Job,Categorey, JobApplication
from django import forms


class JobApplicationForm(forms.ModelForm):
   
    class Meta:
        model = JobApplication
        fields = ('expectedSalary','resume',)