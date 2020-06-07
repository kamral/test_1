from django.shortcuts import render
from .models import Books
# Create your views here.
from  django.views.generic import ListView

class BookListView(ListView):
    model = Books
    template_name = 'book_list.html'
    paginate_by = 2
    queryset = Books.objects.all()
