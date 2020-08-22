from rest_framework import serializers
from .models import Tweet, AuthUser, TweetComment, TweetLike


class TweetListSerializer(serializers.ModelSerializer):
    author_info = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    did_you_comment = serializers.SerializerMethodField()
    did_you_like = serializers.SerializerMethodField()

    class Meta:
        model = Tweet
        fields = ("tweet", "author_info", "comments", "created_at", "likes", "id", "did_you_comment", "did_you_like")

    @staticmethod
    def get_author_info(obj):
        author_info = (
            AuthUser.objects.filter(id=obj.author_id)
            .values("first_name", "last_name", "username", "profile_pic")
            .first()
        )
        return author_info

    @staticmethod
    def get_comments(obj):
        comments = TweetComment.objects.filter(tweet_id=obj.id, flag=1).values(
            "comment", "created_at", "author__first_name", "author_id", "author__last_name"
        )
        return comments

    @staticmethod
    def get_likes(obj):
        likes = TweetLike.objects.filter(tweet_id=obj.id, flag=1).count()
        return likes

    def get_did_you_like(self, obj):
        likes = TweetLike.objects.filter(tweet_id=obj.id, flag=1, author_id=self.context["user_id"])
        return False if not likes else True

    def get_did_you_comment(self, obj):
        comments = TweetComment.objects.filter(tweet_id=obj.id, flag=1, author_id=self.context["user_id"])
        return False if not comments else True
