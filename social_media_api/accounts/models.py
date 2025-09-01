# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class CustomUser(AbstractUser):
    # Users who follow this user
    followers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="user_followers",
        symmetrical=False,
        blank=True,
    )

    # Users this user is following
    following = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="user_following",
        symmetrical=False,
        blank=True,
    )

    def __str__(self):
        return self.username