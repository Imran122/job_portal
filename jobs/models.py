from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.db.models.signals import pre_save
# Create your models here.

class Categorey(models.Model):
    title = models.CharField(max_length=70)

    def __str__(self):
        return self.title
class Job(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100,unique=True, null=True, blank=True)
    categories = models.ForeignKey(Categorey,on_delete=models.CASCADE,null=True, blank=True)
    companyName=models.CharField(max_length=150,null=True, blank=True)
    address=models.CharField(max_length=150,null=True, blank=True)
    experience=models.IntegerField(null=True, blank=True)
    salary=models.IntegerField(null=True, blank=True)
    vacancy=models.IntegerField(null=True, blank=True)
    employmentStatus=models.CharField(max_length=150,null=True, blank=True)
    jobResponsibilities=models.TextField(null=True, blank=True)
    additionalRequirements=models.TextField(null=True, blank=True)
    benefits=models.TextField(null=True, blank=True)
    is_published = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    expiredate = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post',kwargs={ 'slug': self.slug})

def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Job.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug
    
def pre_save_job_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
pre_save.connect(pre_save_job_receiver, Job)