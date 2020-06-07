from books.models import Books
from rest_framework import generics
from .serializers import BooksSerializers

class BooksAPIView(generics.ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializers
