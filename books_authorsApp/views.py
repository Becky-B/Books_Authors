from django.shortcuts import render, HttpResponse, redirect
from .models import *

def index(request):
    context = {
        'all_the_books' : Books.objects.all(),
        'all_the_authors' : Authors.objects.all()
    }
    return render(request, 'index.html', context)

def author(request):
    context = {
        'all_the_books' : Books.objects.all(),
        'all_the_authors' : Authors.objects.all()
    }
    return render(request, 'authorsIndex.html', context)

def books(request):
    context = {
        'all_the_books' : Books.objects.all()
    }
    return render(request, 'books.html', context)

def show_author(request, author_id):
    context ={
        'one_author': Authors.objects.get(id=author_id),
        'all_the_books': Books.objects.all() 
    }
    return render(request,'authors.html', context)

def show_book(request, book_id):
    context ={
        "one_book": Books.objects.get(id=book_id),
        "all_the_authors" : Authors.objects.all()
    }
    return render(request, 'book_detail.html', context)

def AddBook(request):
    addTitle = request.POST['title']
    addGenre = request.POST['genre']
    addYear = request.POST['y_published']
    addAuthor = Authors.objects.get(first_name=request.POST['author'])
    Book.objects.create(title=addTitle, genre=addGenre, y_published=addYear, author=addAuthor)

    return redirect('/books')

def AddAuthor(request):
    addf_name = request.POST['first_name']
    addl_name = request.POST['last_name']
    addNotes = request.POST['notes']
    Authors.objects.create(first_name=addf_name, last_name=addl_name, notes=addNotes)

    return redirect('/authors')