from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment, Tag


# --- User Registration Form ---
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# --- Post Form (for creating and updating blog posts) ---
class PostForm(forms.ModelForm):
    # New field for tags (comma-separated input)
    tags = forms.CharField(
        required=False,
        help_text="Enter tags separated by commas (e.g., Django, Python, Blog)."
    )

    class Meta:
        model = Post
        fields = ["title", "content", "tags"]  # include tags


# --- Comment Form ---
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
