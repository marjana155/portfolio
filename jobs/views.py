from django.shortcuts import render
from .models import Job
# Create your views here.


def home(request):
    job = Job.objects.all()
    return render(request, 'jobs\home.html', {"jobs": job})
