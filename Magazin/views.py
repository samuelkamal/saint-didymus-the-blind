from django.shortcuts import render
from .models import *
# Create your views here.

def Magazin(request):
    context = {
        'carou' : Carousel.objects.all(),
        'mag' : Magazin_Number.objects.all(),
    }
    return render(request, 'Magazin/magazin.html', context)