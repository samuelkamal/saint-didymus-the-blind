from django.urls import path
from . import views

urlpatterns = [
    path('', views.Bachelor, name='bach'),
    path('<str:slug>', views.Bachelor_team, name='team'),
    path('team/<str:slug>', views.Bachelor_term, name='term'),
    path('term/<str:slug>', views.Bachelor_sub, name='sub'),
    path('subject/<str:slug>', views.Bachelor_lec, name='lecs')
]