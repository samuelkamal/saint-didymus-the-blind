from django.shortcuts import render
from .models import *
# Create your views here.

def News_Asv(request):
    return render(request, 'News_Advertisement/news_adv.html', context={
        'news' : News_and_Adv.objects.all()
    })