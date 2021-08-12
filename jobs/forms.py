from .models import Job,Categorey
from django import forms


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('title','categories','companyName','address','experience','salary','vacancy','employmentStatus','jobResponsibilities','additionalRequirements','benefits',)