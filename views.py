from catalogue.stuff.models import Author, Book, Movie, Person

from django.shortcuts import render_to_response, redirect, get_list_or_404, get_object_or_404
import urllib
from django.conf import settings
# from django.views.decorators.cache import cache_control
# from django.db.models import Q

def index(request):
    books = Book.objects.all().order_by('title')
    movies = Movie.objects.all().order_by('title')
    return render_to_response('index.html', {
        'books': books,
        'movies': movies,
    })

def book(request, title, un_id):
    book = get_object_or_404(Book, title_slug=title, id=un_id)
    return render_to_response('book_detail.html', {
        'book': book,
    })

def movie(request, title, un_id):
    movie = get_object_or_404(Movie, title_slug=title, id=un_id)
    return render_to_response('movie_detail.html', {
        'movie': movie,
    })

