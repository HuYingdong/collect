from django.http import JsonResponse
from api.models import Bookmark, Command, UserInfo, UserToken
from django.contrib.auth.models import User
from api.serializers import BookmarkSerializer, UserSerializer, CommandSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from api.permissions import IsOwnerOrReadOnly
from api.throttles import VisitThrottle
from .utils import show_filter, md5


class AuthView(APIView):
    """
    用于用户登录认证
    """
    # throttle_classes = [VisitThrottle, ]

    def post(self, request, *args, **kwargs):
        ret = {'code': 1000, 'msg': None}
        try:
            user = request.data.get('username')
            pwd = request.data.get('password')
            ret['msg'] = '请输入用户名' if not user else '请输入密码' if not pwd else '登录成功'
            if ret['msg'] != '登录成功':
                ret['code'] = 1001
                return JsonResponse(ret)

            obj = UserInfo.objects.filter(username=user, password=pwd).first()
            if not obj:
                ret['code'] = 1001
                ret['msg'] = '用户名或密码错误'
                return JsonResponse(ret)

            # 为登录用户创建token
            token = md5(user)
            # 存在就更新，不存在就创建
            UserToken.objects.update_or_create(user=obj, defaults={'token': token})
            ret['token'] = token
        except Exception as e:
            ret['code'] = 1002
            ret['msg'] = '请求异常'
            import traceback
            traceback.print_exc()

        return JsonResponse(ret)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    用户列表
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BookmarkViewSet(viewsets.ModelViewSet):
    """
    书签列表
    """
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

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
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

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
