from django.urls import path
from . import views

urlpatterns = [
    path('dar-el-nashr/', views.Dar_El_Nashr, name='dar'),
    path('dar-el-nashr/<str:slug>/<int:id>', views.Book_Details, name='books')
]