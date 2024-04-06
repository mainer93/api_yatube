from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied

from posts.models import Post, Group, Comment
from .serializers import PostSerializer, GroupSerializer, CommentSerializer


class PermissionMixin:

    def check_permission(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Изменение/удаление чужого '
                                   'контента запрещено!')

    def perform_update(self, serializer):
        instance = serializer.instance
        self.check_permission(instance)
        super().perform_update(serializer)

    def perform_destroy(self, instance):
        self.check_permission(instance)
        instance.delete()


class CommentMixin:

    def get_queryset(self):
        post_id = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        return Comment.objects.filter(post=post_id)

    def perform_create(self, serializer):
        post_id = get_object_or_404(Post, id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post_id)


class PostViewSet(PermissionMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(PermissionMixin, CommentMixin, viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
