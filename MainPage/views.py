from django.shortcuts import render
from .models import *
# Create your views here.

def Home(request):
    context = {
        'mainPic' : Main_Pic.objects.all(),
        'darELnashr' : Dar_El_Nashr.objects.all(),
        'magazin' : Magazin.objects.all(),
        'library' : Library.objects.all(),
        'whoWeAre' : Who_We_Are.objects.all(),
        'followUs' : Follow_Us.objects.all(),
        'dip' : Dibloma.objects.all(),
        'bach' : Bachelor.objects.all(),
        'spe_cour' : Specialized_Courses.objects.all(),
        'post' : Postgraduate.objects.all()
    }
    return render(request, 'MainPage/home.html', context)

