from rest_framework import generics, permissions
from rest_framework.exceptions import NotFound
from .models import Book
from .serializers import BookSerializer
from rest_framework import serializers

# 1. List all books (Read-only for everyone)
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Anyone can read

# 2. Retrieve a single book by ID (Read-only for everyone)
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# 3. Create a new book (Auth required)
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save()

# 4. Update an existing book (Auth required)
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Get book ID from request data (e.g., JSON payload)
        book_id = self.request.data.get('id')
        if not book_id:
            raise serializers.ValidationError({"id": "Book ID is required in the request body."})
        try:
            return self.queryset.get(pk=book_id)
        except Book.DoesNotExist:
            raise NotFound("Book not found.")

    def perform_update(self, serializer):
        # Custom validation: prevent title from being blank
        if not serializer.validated_data.get('title'):
            raise serializers.ValidationError({"title": "Title cannot be empty."})
        serializer.save()

# 5. Delete a book (Auth required)
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Get book ID from request data (e.g., JSON payload)
        book_id = self.request.data.get('id')
        if not book_id:
            raise serializers.ValidationError({"id": "Book ID is required in the request body."})
        try:
            return self.queryset.get(pk=book_id)
        except Book.DoesNotExist:
            raise NotFound("Book not found.")
