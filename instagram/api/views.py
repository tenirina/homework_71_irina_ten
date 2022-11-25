from rest_framework.viewsets import ModelViewSet, ViewSet
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.response import Response
from rest_framework.permissions import SAFE_METHODS
from django.http import HttpResponse
from rest_framework import status

from api.serializers import PostSerializer
from posts.models import Post
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, BasePermission


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create_likes(self, request, *args, **kwargs):
        user = request.user
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        if not post.user_likes.filter(username=user).exists():
            user.liked_posts.add(post)
            post.count_like += 1
            post.save()
        return Response(status=status.HTTP_200_OK)

    def delete_likes(self, request, *args, **kwargs):
        user = request.user
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        if post.user_likes.filter(username=user):
            user.liked_posts.remove(post)
            post.count_like -= 1
            post.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_permissions(self):
        if 'likes' in self.request.path:
            self.permission_classes = [IsAuthenticated, ]
            return super(PostViewSet, self).get_permissions()
        elif len(self.request.path.split('/')) == 5:
            post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
            if post.author == self.request.user:
                self.permission_classes = [IsAuthenticated, ]
            else:
                self.permission_classes = [ReadOnly, ]
            return super(PostViewSet, self).get_permissions()
        self.permission_classes = [IsAuthenticatedOrReadOnly, ]
        return super(PostViewSet, self).get_permissions()
