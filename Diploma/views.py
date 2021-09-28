from django.contrib.auth import login
from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def Diploma(request):
    return render(request, 'Diploma/dip.html', context={
        'sub' : Subject.objects.all(),
        'ad' : Ads.objects.all(),
    })

@login_required
def Diploma_sub(request, slug):
    return render(request, 'Diploma/sub.html', context={
        'less' : Lecture.objects.all().filter(Subject__Slug=slug),
        'sub' : Subject.objects.all().filter(Slug=slug)
    })

@login_required
def Diploma_lec(request, slug):
    lecDetail = Lecture.objects.get(Slug=slug)
    return render(request, 'Diploma/lec.html', context={
        'lec' : lecDetail
    })