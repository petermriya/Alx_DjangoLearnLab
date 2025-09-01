from rest_framework import serializers
from .models import Post, Like


class PostSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ["id", "author", "content", "created_at", "like_count"]

    def get_like_count(self, obj):
        return obj.likes.count()