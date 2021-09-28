from django.urls import path
from . import views

urlpatterns = [
    path('', views.Postgraduate, name='pos'),
    path('<str:slug>', views.Postgraduate_sub, name='possubs'),
    path('lecture/<str:slug>', views.Postgraduate_lec, name='poslec')
]