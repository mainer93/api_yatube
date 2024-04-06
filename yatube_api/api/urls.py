from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('api/v1/posts/',
         PostViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/posts/<int:post_id>/',
         PostViewSet.as_view({'get': 'retrieve', 'put': 'update',
                              'patch': 'partial_update',
                              'delete': 'destroy'})),
    path('api/v1/groups/', GroupViewSet.as_view({'get': 'list'})),
    path('api/v1/groups/<int:group_id>/',
         GroupViewSet.as_view({'get': 'retrieve'})),
    path('api/v1/posts/<int:post_id>/comments/',
         CommentViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/posts/<int:post_id>/comments/<int:pk>/',
         CommentViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                 'patch': 'partial_update',
                                 'delete': 'destroy'})),
]
