from django.urls import path
from . import views

urlpatterns = [
    path('', views.grad_year, name='grad'),
    path('<str:slug>', views.stud, name='stud')
]