# Register your models here.
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')     # Show these fields in the admin list
    list_filter = ('author', 'publication_year')               # Add filters on the right
    search_fields = ('title', 'author')                        # Add search box

admin.site.register(Book, BookAdmin)
