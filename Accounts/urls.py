from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.signup, name='login'),
    path('profile/', views.more_info, name='profile'),
    path('courses/', views.courses, name='courses'),
    path('logout/', views.Logout, name='logout')
]