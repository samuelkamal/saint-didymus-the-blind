from django.urls import path
from . import views

urlpatterns = [
    path('', views.Spe, name='specour'),
    path('<str:slug>', views.Spe_sub, name='spesub'),
    path('lecture/<str:slug>', views.Spe_lec, name='spelec')
]