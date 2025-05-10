from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from .models import Book


def index(request):
    all_books = Book.objects.all().order_by("-rating")
    num_books = all_books.count()
    avg_rating = all_books.aggregate(Avg("rating"))

    return render(request, "book_outlet/index.html", context={
        "books": all_books,
        "total_numbers_of_books": num_books,
        "average_rating": avg_rating,
    })


def book_detail(request, slug):
    # book = Book.objects.get(slug=slug)
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book_detail.html", context={
        "title": book.title,
        "author": book.author,
        "rating": book.rating,
        "is_best": book.is_bestselling
    })
