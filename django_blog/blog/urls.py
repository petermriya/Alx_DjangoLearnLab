from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView,
    CommentCreateView, CommentUpdateView, CommentDeleteView
)

urlpatterns = [
    # Auth routes
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="blog/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),

    # CRUD Post routes
    path("", PostListView.as_view(), name="post-list"),                          # list all
    path("post/new/", PostCreateView.as_view(), name="post-create"),             # create
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),        # detail
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"), # update
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"), # delete

    # ✅ Comment routes (fixed)
    path("post/<int:pk>/comments/new/", CommentCreateView.as_view(), name="comment-create"),
    path("comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment-update"),
    path("comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"),
]
