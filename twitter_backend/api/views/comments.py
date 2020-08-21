# Django Imports
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Models
from ..models import TweetComment


class CommentsView(APIView):
    @staticmethod
    def post(request):
        try:

            user: int = request.requested_by
            tweet_id: int = request.data.get("tweet_id", None)
            comment: str = request.data.get("comment", None)

            if not tweet_id or not comment:
                return Response({"message": "Tweet ID missing"}, status=status.HTTP_400_BAD_REQUEST)

            comment_obj = TweetComment.objects.create(tweet_id=tweet_id, author_id=user, comment=comment)

            if comment_obj:
                res: dict = {
                    "message": "Comment posted successfully",
                    "status": status.HTTP_201_CREATED,
                    "result": {"comment_id": comment_obj.id},
                }
                return Response(res, res["status"])
            else:
                raise Exception
        except:
            res: dict = {
                "message": "failed to post",
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "result": {},
            }
            return Response(res, res["status"])

