from django.shortcuts import render
from .models import Book
# Create your views here.
from django.views.generic import ListView


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
