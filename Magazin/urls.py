from django.urls import path
from . import views

urlpatterns = [
    path('magazin/', views.Magazin, name='magazin'),
]