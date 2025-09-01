# accounts/urls.py
from django.urls import path
from .views import FollowUserView, UnfollowUserView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Existing authentication routes
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", views.register_view, name="register"),

    # New follow management routes
    path("follow/<int:user_id>/", FollowUserView.as_view(), name="follow-user"),
    path("unfollow/<int:user_id>/", UnfollowUserView.as_view(), name="unfollow-user"),
]
