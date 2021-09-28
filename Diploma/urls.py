from django.urls import path
from . import views

urlpatterns = [
    path('', views.Diploma, name='dip'),
    path('<str:slug>', views.Diploma_sub, name='subs'),
    path('lecture/<str:slug>', views.Diploma_lec, name='lec')
]