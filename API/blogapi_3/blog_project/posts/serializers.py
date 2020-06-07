from rest_framework import serializers
from .models import Posts
from django.contrib.auth import get_user_model

class PostsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Posts
        fields=('id','author','title', 'body', 'created_at')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields=('id','username',)