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
    # ✅ Field for entering tags (comma-separated input)
    tags = forms.CharField(
        required=False,
        help_text="Enter tags separated by commas (e.g., Django, Python, Blog)."
    )

    class Meta:
        model = Post
        fields = ["title", "content", "tags"]

    def save(self, commit=True):
        post = super().save(commit=False)

        if commit:
            post.save()

        # ✅ Handle tag saving
        tags_str = self.cleaned_data.get("tags", "")
        if tags_str:
            tag_list = [tag.strip() for tag in tags_str.split(",") if tag.strip()]
            post.tags.set(*tag_list)  # Taggit allows setting multiple tags at once
        else:
            post.tags.clear()

        return post


# --- Comment Form ---
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
