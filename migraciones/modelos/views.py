from django.shortcuts import render
from .models import Author, Book

def index(request):
    authors = Author.objects.all()
    books = Book.objects.all()
    context = {
        'authors': authors,
        'books': books
    }
    return render(request, 'modelos/index.html', context)