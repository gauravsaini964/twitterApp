from rest_framework import serializers
from .models import Tweet, AuthUser, TweetComment


class TweetListSerializer(serializers.ModelSerializer):
    author_info = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = ("tweet", "author_info", "comments", "created_at")

    @staticmethod
    def get_author_info(obj):
        author_info = AuthUser.objects.filter(id=obj.author_id).values("first_name", "last_name", "username").first()
        return author_info

    @staticmethod
    def get_comments(obj):
        comments = TweetComment.objects.filter(tweet_id=obj.id, flag=1).values(
            "comment", "created_at", "author__first_name", "author_id", "author__last_name"
        )
        return comments
