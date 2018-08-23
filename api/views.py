# version_1: regular Django views
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# from api.models import Bookmark
# from api.serializers import BookmarkSerializer
#
#
# @csrf_exempt
# def bookmark_list(request):
#     if request.method == 'GET':
#         bookmarks = Bookmark.objects.all()
#         serializer = BookmarkSerializer(bookmarks, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = BookmarkSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
#
# @csrf_exempt
# def bookmark_detail(request, pk):
#     try:
#         bookmark = Bookmark.objects.get(pk=pk)
#     except Bookmark.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = BookmarkSerializer(bookmark)
#         return JsonResponse(serializer.data)
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = BookmarkSerializer(bookmark, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         bookmark.delete()
#         return HttpResponse(status=204)


# version_2: rest_framework @api_view
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from api.models import Bookmark
# from api.serializers import BookmarkSerializer
#
#
# @api_view(['GET', 'POST'])
# def bookmark_list(request, format=None):
#     if request.method == 'GET':
#         bookmarks = Bookmark.objects.all()
#         serializer = BookmarkSerializer(bookmarks, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = BookmarkSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# def bookmark_detail(request, pk, format=None):
#     try:
#         bookmark = Bookmark.objects.get(pk=pk)
#     except Bookmark.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = BookmarkSerializer(bookmark)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = BookmarkSerializer(bookmark, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         bookmark.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# version_3: cbv class-based views
# from api.models import Bookmark
# from api.serializers import BookmarkSerializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
#
#
# class BookmarkList(APIView):
#
#     @staticmethod
#     def get(request, format=None):
#         bookmarks = Bookmark.objects.all()
#         serializer = BookmarkSerializer(bookmarks, many=True)
#         return Response(serializer.data)
#
#     @staticmethod
#     def post(request, format=None):
#         serializer = BookmarkSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class BookmarkDetail(APIView):
#
#     @staticmethod
#     def get_object(pk):
#         try:
#             return Bookmark.objects.get(pk=pk)
#         except Bookmark.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         bookmark = self.get_object(pk=pk)
#         serializer = BookmarkSerializer(bookmark)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         bookmark = self.get_object(pk=pk)
#         serializer = BookmarkSerializer(bookmark, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         bookmark = self.get_object(pk=pk)
#         bookmark.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# version_4: Using mixins
# from api.models import Bookmark
# from api.serializers import BookmarkSerializer
# from rest_framework import mixins
# from rest_framework import generics
#
#
# class BookmarkList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Bookmark.objects.all()
#     serializer_class = BookmarkSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class BookmarkDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
#                      mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Bookmark.objects.all()
#     serializer_class = BookmarkSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# version_5: Using generic class-based views
# from api.models import Bookmark
# from api.serializers import BookmarkSerializer, UserSerializer
# from rest_framework import generics
# from django.contrib.auth.models import User
# from rest_framework import permissions
# from api.permissions import IsOwnerOrReadOnly
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework.reverse import reverse
#
#
# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format),
#         'bookmarks': reverse('bookmark-list', request=request, format=format)
#     })
#
#
# # bookmark
# class BookmarkList(generics.ListCreateAPIView):
#     queryset = Bookmark.objects.all()
#     serializer_class = BookmarkSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
#
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)
#
#
# class BookmarkDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Bookmark.objects.all()
#     serializer_class = BookmarkSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
#
#
# # user
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# version_6: Using ViewSets & Routers
from api.models import Bookmark
from django.contrib.auth.models import User
from api.serializers import BookmarkSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from api.permissions import IsOwnerOrReadOnly


@api_view(['GET'])  # api/urls.py version_6.2 不需要api_view，删除。
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'bookmarks': reverse('bookmark-list', request=request, format=format)
    })


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

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
