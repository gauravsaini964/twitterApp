# Django Imports
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Models
from ..models import TweetLike


class LikesView(APIView):
    @staticmethod
    def post(request):
        try:
            user: int = request.requested_by
            tweet_id: int = request.data.get("tweet_id", None)

            if not tweet_id:
                return Response({"message": "Tweet ID missing"}, status=status.HTTP_400_BAD_REQUEST)

            like_obj = TweetLike.objects.filter(tweet_id=tweet_id, author_id=user, flag=True).first()
            if not like_obj:
                like_obj = TweetLike.objects.create(tweet_id=tweet_id, author_id=user)

            if like_obj:
                res: dict = {
                    "message": "Like posted successfully",
                    "status": status.HTTP_201_CREATED,
                    "result": {"like": like_obj.id},
                }
                return Response(res, res["status"])
            else:
                raise Exception
        except Exception as e:
            res: dict = {
                "message": "failed to post",
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "result": {},
            }
            return Response(res, res["status"])

    @staticmethod
    def delete(request):
        user = request.requested_by
        tweet_id: int = request.data.get("tweet_id")

        if not tweet_id:
            return Response({"message": "Tweet ID missing"}, status=status.HTTP_400_BAD_REQUEST)

        if TweetLike.objects.filter(tweet_id=tweet_id, author_id=user).update(flag=False):
            res = {"message": "Like deleted successfully", "status": status.HTTP_200_OK, "result": []}
            return Response(res, res["status"])
        else:
            res = {"message": "Failed to delete Like ", "status": status.HTTP_500_INTERNAL_SERVER_ERROR, "result": []}
            return Response(res, res["status"])
