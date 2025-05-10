from django.shortcuts import render

from .models import Book


def index(request):
    all_books = Book.objects.all()
    return render(request, "book_outlet/index.html", context={
        "books": all_books
    })


def book_detail(request, id):
    book = Book.objects.get(pk=id)
    return render(request, "book_outlet/book_detail.html", context={
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_best": book.is_bestselling
    })
