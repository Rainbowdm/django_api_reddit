from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # poster = serializers.ReadOnlyField(source='poster.username')
    # poster_id = serializers.ReadOnlyField(source='poster.id')
    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)
