from rest_framework import serializers
from lifebits.models import User, List, Post, Item

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name', 'last_name', 'handle', 'email',
            'created_at')

class ListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = List
        fields = ('id', 'created_at', 'title', 'user', 'slug')

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'created_at', 'post_type', 'content_image',
            'content_text', 'item')

class ItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = ('id', 'name', 'created_at', 'views', 'favorited', 'status',
            'completion', 'ilist')

