# Django Imports
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status

# Models
from ..models import Tweet

# Misc Imports
from ..serializer import TweetListSerializer


class TweetsView(ViewSet):
    @staticmethod
    def list(request):
        try:
            search: str = request.GET.get("search", None)
            tweets = Tweet.objects.filter(flag=True).order_by("-id")
            if search:
                tweets = Tweet.objects.filter(tweet__icontains=search, flag=True).order_by("-id")
            response_data = TweetListSerializer(instance=tweets, many=True).data
            res = {"message": "Data fetched successfully", "status": status.HTTP_200_OK, "result": response_data}
            return Response(res, res["status"])

        except:
            res = {"message": "Something went wrong", "status": status.HTTP_500_INTERNAL_SERVER_ERROR, "result": []}
            return Response(res, res["status"])

    @staticmethod
    def create(request):
        try:
            tweet: str = request.data.get("tweet", "")
            user: int = request.requested_by

            tweet_obj = Tweet.objects.create(tweet=tweet, author_id=user)
            if tweet_obj:
                result = {
                    "tweet_id": tweet_obj.id,
                }
                res: dict = {
                    "message": "Tweet created successfully",
                    "status": status.HTTP_201_CREATED,
                    "result": result,
                }
                return Response(res, res["status"])
            else:
                raise Exception
        except:
            res: dict = {
                "message": "Something went wrong",
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "result": {},
            }
            return Response(res, res["status"])

    @staticmethod
    def update(request, pk=None):
        user = request.requested_by
        tweet: str = request.data.get("tweet", None)
        update_obj = Tweet.objects.filter(id=pk, author_id=user).update(tweet=tweet)
        if update_obj:
            res: dict = {
                "message": "Tweet updated successfully",
                "status": status.HTTP_200_OK,
                "result": {"tweet_id": update_obj},
            }
            return Response(res, res["status"])
        else:
            res: dict = {
                "message": "Failed to update Tweet",
                "status": status.HTTP_400_BAD_REQUEST,
                "result": {},
            }
            return Response(res, res["status"])

    @staticmethod
    def destroy(request, pk):
        user = request.requested_by
        if Tweet.objects.filter(id=pk, author_id=user).update(flag=0):
            res = {"message": "tweet deleted successfully", "status": status.HTTP_200_OK, "result": []}
            return Response(res, res["status"])
        else:
            res = {"message": "Failed to delete tweet ", "status": status.HTTP_500_INTERNAL_SERVER_ERROR, "result": []}
            return Response(res, res["status"])

    @staticmethod
    def retrieve(request, pk=None):
        try:
            tweets = Tweet.objects.filter(id=pk, flag=True).first()
            response_data = TweetListSerializer(instance=tweets).data
            res = {"message": "Data fetched successfully", "status": status.HTTP_200_OK, "result": response_data}
            return Response(res, res["status"])
        except:
            res = {"message": "Something went wrong", "status": status.HTTP_500_INTERNAL_SERVER_ERROR, "result": []}
            return Response(res, res["status"])
