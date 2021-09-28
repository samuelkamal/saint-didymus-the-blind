from django.core.paginator import Paginator
from django.shortcuts import render
from .models import *
# Create your views here.

def Library(request):
    search = Add_Book.objects.all()
    title = None
    category = None
    if 'search_' in request.GET:
        title = request.GET['search_']
        if title:
            search = search.filter(Title__icontains=title)


    if 'cat' in request.GET:
        category = request.GET['cat']
        if category:
            search = search.filter(Category__id=category)

    books = search
    paginator = Paginator(books, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'book' : page_obj,
        'adv' : Advertisement.objects.all(),
        'cat' : Categories.objects.all(),
    }
    return render(request, 'Library/library.html', context)


def Book_Details(request, slug, id):
    bookDetail = Add_Book.objects.get(id=id, Slug=slug)
    context = {
        'books' : bookDetail,
    }
    return render(request, 'Library/book_details.html', context)