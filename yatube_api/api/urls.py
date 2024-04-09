from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .constants import Constants
from .views import PostViewSet, GroupViewSet, CommentViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)

urlpatterns = [
    path(f'{Constants.VERSION}/', include(router.urls)),
    path(f'{Constants.VERSION}/api-token-auth/', views.obtain_auth_token),
]
