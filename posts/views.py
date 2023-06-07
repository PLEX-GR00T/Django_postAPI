# from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post
from .serializers import PostSerializer
from .permissions import IsAuthorOrNot

# Create your views here.
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class PostRUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrNot]

class PostLikeUnlikeView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        user = request.user
        post:Post = self.get_object()

        if user in post.liked_by.all():
            post.liked_by.remove(user)
            s = 'Post Unliked'
        else:
            post.liked_by.add(user)
            s = 'Post Liked'
        
        return Response(
            {'status': s,'post': PostSerializer(post).data}, 
            status=status.HTTP_200_OK,
        )