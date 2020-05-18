from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books', views.books),
    path('books/<int:book_id>', views.show_book),
    path('add_author', views.AddAuthor),
    path('add_book', views.AddBook),
    path('authors/<int:author_id>', views.show_author),
    path('authors', views.author)
]