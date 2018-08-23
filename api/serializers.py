from rest_framework import serializers
from api.models import Bookmark
from django.contrib.auth.models import User


class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    detail = serializers.HyperlinkedIdentityField(view_name='bookmark-detail', format='html')

    class Meta:
        model = Bookmark
        fields = ('detail', 'issue', 'url', 'sort')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # bookmarks = serializers.PrimaryKeyRelatedField(many=True, queryset=Bookmark.objects.all())
    bookmarks = serializers.HyperlinkedRelatedField(many=True, view_name='bookmark-detail', read_only=True)

    class Meta:
        model = User
        # fields = '__all__'
        fields = ('url', 'id', 'username', 'bookmarks')
