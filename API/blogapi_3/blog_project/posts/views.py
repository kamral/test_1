from django.contrib.auth import get_user_model
from rest_framework import viewsets # new
from .models import Posts
from .permissions import IsAuthorOrReadOnly
from .serializers import PostsSerializers, UserSerializer

class PostViewSet(viewsets.ModelViewSet): # new
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Posts.objects.all()
    serializer_class = PostsSerializers

class UserViewSet(viewsets.ModelViewSet): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer