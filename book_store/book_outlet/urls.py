from django.urls import path

from .views import *

urlpatterns = [
    path("", index, name='all-books'),
    path("<int:id>", book_detail, name='book-detail')
]
