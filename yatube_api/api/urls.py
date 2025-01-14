from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

api_v1_router = DefaultRouter()
api_v1_router.register("posts", PostViewSet, basename="posts")
api_v1_router.register("groups", GroupViewSet, basename="groups")
api_v1_router.register(r"posts/(?P<post_id>\d+)/comments", CommentViewSet, basename="comments")

urlpatterns = [
    path("api-token-auth/", views.obtain_auth_token),
    path("", include(api_v1_router.urls)),
]
