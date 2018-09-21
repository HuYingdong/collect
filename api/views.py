from api.models import Bookmark, Command
from django.contrib.auth.models import User
from api.serializers import BookmarkSerializer, UserSerializer, CommandSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from api.permissions import IsOwnerOrReadOnly
from .helper import show_filter


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    用户列表
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)


class BookmarkViewSet(viewsets.ModelViewSet):
    """
    书签列表
    """
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly,)

    list_show = ['issue', 'url', 'detail']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = show_filter(serializer.data, self.list_show)
            return self.get_paginated_response(data)

        serializer = self.get_serializer(queryset, many=True)
        data = show_filter(serializer.data, self.list_show)
        return Response(data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommandViewSet(viewsets.ModelViewSet):
    """
    命令列表
    """
    queryset = Command.objects.all()
    serializer_class = CommandSerializer
    permission_classes = (permissions.IsAuthenticated, IsOwnerOrReadOnly)

    show = ['issue', 'cmd', 'detail']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            data = show_filter(serializer.data, self.show)
            return self.get_paginated_response(data)

        serializer = self.get_serializer(queryset, many=True)
        data = show_filter(serializer.data, self.show)
        return Response(data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
