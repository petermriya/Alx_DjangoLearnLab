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

    # CRUD Post routes (match exactly what Django expects)
    path("", PostListView.as_view(), name="post-list"),                       # list all
    path("post/new/", PostCreateView.as_view(), name="post-create"),          # create
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),     # detail
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"), # update
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"), # delete
]

