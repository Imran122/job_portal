
from django.contrib import admin
from .models import Categorey,Job, JobApplication
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','is_published','companyName')
    list_display_links = ('id', 'title',)
    
   
class CategoreyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)

admin.site.register(Job,JobAdmin)

admin.site.register(Categorey, CategoreyAdmin)
admin.site.register(JobApplication)
