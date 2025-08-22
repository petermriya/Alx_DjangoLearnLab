from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView, PostDetailView,
    PostCreateView, PostUpdateView, PostDeleteView
)

urlpatterns = [
    # Auth routes
    path("login/", auth_views.LoginView.as_view(template_name="blog/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="blog/logout.html"), name="logout"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),

    # CRUD Post routes
    path("posts/", PostListView.as_view(), name="post-list"),                # /posts/
    path("posts/new/", PostCreateView.as_view(), name="post-create"),        # /posts/new/
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),   # /posts/1/
    path("posts/<int:pk>/edit/", PostUpdateView.as_view(), name="post-update"),   # /posts/1/edit/
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"), # /posts/1/delete/
]
