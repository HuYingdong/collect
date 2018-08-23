from rest_framework import serializers
from api.models import Bookmark, Command
from django.contrib.auth.models import User


class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    detail = serializers.HyperlinkedIdentityField(view_name='bookmark-detail', format='html')

    class Meta:
        model = Bookmark
        fields = '__all__'


class CommandSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    detail = serializers.HyperlinkedIdentityField(view_name='command-detail', format='html')

    class Meta:
        model = Command
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    bookmarks = serializers.HyperlinkedRelatedField(many=True, view_name='bookmark-detail', read_only=True)
    commands = serializers.HyperlinkedRelatedField(many=True, view_name='command-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'bookmarks', 'commands')
