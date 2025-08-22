from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, Tag
from .forms import PostForm, CommentForm


# --- Post Views ---
class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"
    ordering = ["-published_date"]


class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        self.handle_tags(form.cleaned_data.get("tags", ""))
        return response

    def handle_tags(self, tags_string):
        if tags_string:
            tag_names = [tag.strip() for tag in tags_string.split(",") if tag.strip()]
            for name in tag_names:
                tag_obj, created = Tag.objects.get_or_create(name=name)
                self.object.tags.add(tag_obj)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "blog/post_form.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        self.object.tags.clear()  # clear old tags
        self.handle_tags(form.cleaned_data.get("tags", ""))
        return response

    def handle_tags(self, tags_string):
        if tags_string:
            tag_names = [tag.strip() for tag in tags_string.split(",") if tag.strip()]
            for name in tag_names:
                tag_obj, created = Tag.objects.get_or_create(name=name)
                self.object.tags.add(tag_obj)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"
    template_name = "blog/post_confirm_delete.html"

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
