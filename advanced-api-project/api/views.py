from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from datetime import date
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book, BlogPost
from .serializers import BookSerializer, BlogPostSerializer

# -------------------- BOOK VIEWS --------------------

# List all books (read-only for everyone, write requires auth)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# Retrieve a single book by ID (read-only for everyone)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# Create a new book (only logged-in users can create)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        publication_year = request.data.get('publication_year')
        if publication_year and int(publication_year) < 1500:
            return Response(
                {"error": "Publication year must be after 1500."},
                status=status.HTTP_400_BAD_REQUEST
            )
        return super().create(request, *args, **kwargs)


# Update an existing book (only logged-in users can update)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        publication_year = request.data.get('publication_year')
        if publication_year:
            current_year = date.today().year
            if int(publication_year) > current_year:
                return Response(
                    {"error": "Publication year cannot be in the future."},
                    status=status.HTTP_400_BAD_REQUEST
                )
        return super().update(request, *args, **kwargs)


# Delete a book (only logged-in users can delete)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# -------------------- BLOGPOST VIEWS --------------------

# List & Create
class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Retrieve, Update & Delete
class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
