from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Post, Comment


# --- User Registration Form ---
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


# --- Post Form (for creating and updating blog posts) ---
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]  # author is set automatically in the view


# --- Comment Form (for creating and editing comments) ---
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]  # author and post are set in the view
