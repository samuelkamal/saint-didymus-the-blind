from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
# Create your views here.

@login_required
def Postgraduate(request):
    return render(request, 'Postgraduate/posgra.html', context={
        'sub' : Subject.objects.all(),
        'ad' : Ads.objects.all(),
    })

@login_required
def Postgraduate_sub(request, slug):
    return render(request, 'Postgraduate/possub.html', context={
        'less' : Lecture.objects.all().filter(Subject__Slug=slug),
        'sub' : Subject.objects.all().filter(Slug=slug)
    })

@login_required
def Postgraduate_lec(request, slug):
    lecDetail = Lecture.objects.get(Slug=slug)
    return render(request, 'Postgraduate/poslec.html', context={
        'lec' : lecDetail
    })