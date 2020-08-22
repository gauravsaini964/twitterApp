from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password

# Misc Imports
from rest_framework_jwt.authentication import api_settings
from api.utils.jwt_generate import jwt_payload_handler

# Models Imports
from api.models import AuthUser

JWT_ENCODER = api_settings.JWT_ENCODE_HANDLER


class LoginOrRegisterView(APIView):
    @staticmethod
    def post(request):
        try:
            first_name: str = request.data.get("first_name", None)
            last_name: str = request.data.get("last_name", None)
            email: str = request.data.get("email", None)
            password: str = request.data.get("password", "1111")
            profile_pic: str = request.data.get("profile_pic", "")
            hashed_pass: str = make_password(password)
            user_name: str = email.split("@")[0]

            user_info = {
                "password": hashed_pass,
                "email": email,
                "last_name": last_name,
                "username": user_name,
                "first_name": first_name,
                "profile_pic": profile_pic,
            }

            user_obj = AuthUser.objects.filter(email=email, username=user_name).first()
            http_status = status.HTTP_200_OK
            if not user_obj:
                http_status = status.HTTP_201_CREATED
                user_obj = AuthUser.objects.create(**user_info)

            user_detail = {
                "name": f"{user_obj.first_name} {user_obj.last_name}",
                "email": user_obj.email,
                "id": user_obj.id,
                "pic": user_obj.profile_pic,
                "token": JWT_ENCODER(jwt_payload_handler(user_obj)),
            }

            if user_obj:
                response = {
                    "message": "User signed up successfully",
                    "status": http_status,
                    "result": user_detail,
                }
            else:
                response = {
                    "message": "Could not create entry",
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                    "result": {},
                }
            return Response(response, response["status"])

        except:
            response = {
                "message": "Something went wrong",
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "result": {},
            }
            return Response(response, response["status"])


class LoginView(APIView):
    @staticmethod
    def post(request):
        try:
            user = request.requested_by

            user_obj = AuthUser.objects.filter(id=user).first()
            if not user_obj:
                response = {
                    "message": "User not found",
                    "status": status.HTTP_404_NOT_FOUND,
                    "result": {},
                }
                return Response(response, response["status"])

            user_detail = {
                "name": f"{user_obj.first_name} {user_obj.last_name}",
                "email": user_obj.email,
                "id": user_obj.id,
                "pic": user_obj.profile_pic,
                "token": JWT_ENCODER(jwt_payload_handler(user_obj)),
            }

            response = {
                "message": "User signed up successfully",
                "status": status.HTTP_200_OK,
                "result": user_detail,
            }
            return Response(response, response["status"])

        except:
            response = {
                "message": "Something went wrong",
                "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
                "result": {},
            }
            return Response(response, response["status"])

