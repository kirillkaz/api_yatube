from rest_framework import serializers

from .models import Comment, Group, Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        fields = ("id", "text", "author", "pub_date")
        model = Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "title")
        model = Group


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        fields = ("id", "author", "post", "text", "created")
        model = Comment
