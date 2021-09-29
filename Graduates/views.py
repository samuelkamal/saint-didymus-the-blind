from django.shortcuts import render
from .models import *
# Create your views here.

def grad_year(request):
    return render(request, 'graduates/grad.html', context={
        'year' : Year.objects.all()
    })

def stud(request, slug):
    return render(request, 'graduates/stud.html', context={
        'stud' : Students.objects.all().filter(Year__Slug=slug),
        'year' : Year.objects.all().filter(Slug=slug)
    })