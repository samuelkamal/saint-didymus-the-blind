from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
# Create your views here.

@login_required
def Bachelor(request):
    return render(request, 'Bachelor/bach.html', context={
        'ad' : Ads.objects.all(),
        'team' : Team.objects.all()
    })

@login_required
def Bachelor_team(request, slug):
    return render(request, 'Bachelor/team.html', context={
        'term' : Term.objects.all().filter(Team__Slug=slug)
    })

@login_required
def Bachelor_term(request, slug):
    return render(request, 'Bachelor/term.html', context={
        'sub' : Subject.objects.all().filter(Term__Slug=slug)
    })

@login_required
def Bachelor_sub(request, slug):
    return render(request, 'Bachelor/sub.html', context={
        'less' : Lecture.objects.all().filter(Subject__Slug=slug),
        'sub' : Subject.objects.all().filter(Slug=slug)
    })

@login_required
def Bachelor_lec(request, slug):
    lecDetail = Lecture.objects.get(Slug=slug)
    return render(request, 'Bachelor/lec.html', context={
        'lec' : lecDetail
    })