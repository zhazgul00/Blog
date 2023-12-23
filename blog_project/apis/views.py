from rest_framework import generics
from blog.models import Post
from .serializers import BlogSerializer

class BlogAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer
    
class BlogApiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = BlogSerializer
