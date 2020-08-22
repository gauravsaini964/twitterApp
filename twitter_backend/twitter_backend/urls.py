"""twitter_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import SimpleRouter
from api.views import auth, tweet, comments, likes

router_obj = SimpleRouter()
router_obj.register(
    "tweet", tweet.TweetsView, basename="tweet_view",
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("v1/auth/", auth.LoginOrRegisterView.as_view()),
    path("v1/login/", auth.LoginView.as_view()),
    path("v1/comment/", comments.CommentsView.as_view()),
    path("v1/likes/", likes.LikesView.as_view()),
    path("", include(router_obj.urls)),
]
