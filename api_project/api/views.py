from django.shortcuts import render
from rest_framework import generics

# Create your views here.
# api/views.py

# api/views.py

# api/views.py

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
