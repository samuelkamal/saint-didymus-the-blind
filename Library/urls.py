from django.urls import path
from . import views

urlpatterns = [
    path('library/', views.Library, name='lib'),
    path('library/<str:slug>/<int:id>', views.Book_Details, name='book')
]