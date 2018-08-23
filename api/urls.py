# from django.conf.urls import url
# from rest_framework.urlpatterns import format_suffix_patterns
# from api import views

# version_1: fbv function-based urls
# urlpatterns = [
#     url(r'^bookmarks/$', views.bookmark_list),
#     url(r'^bookmarks/(?P<pk>[0-9]+)/$', views.bookmark_detail),
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)


# version_5: cbv class-based urls
# urlpatterns = [
#     url(r'^$', views.api_root),
#     url(r'^bookmarks/$', views.BookmarkList.as_view(), name='bookmark-list'),
#     url(r'^bookmarks/(?P<pk>[0-9]+)/$', views.BookmarkDetail.as_view(), name='bookmark-detail'),
#     url(r'^users/$', views.UserList.as_view(), name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
# ]
# urlpatterns = format_suffix_patterns(urlpatterns)


# version_6.1: Using ViewSets & Routers
# from api.views import BookmarkViewSet, UserViewSet, api_root
#
# bookmark_list = BookmarkViewSet.as_view({
#     'get': 'list',
#     'post': 'create',
# })
# bookmark_detail = BookmarkViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy',
# })
#
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
#
# urlpatterns = format_suffix_patterns([
#     url(r'^$', api_root),
#     url(r'^bookmarks/$', bookmark_list, name='bookmark-list'),
#     url(r'^bookmarks/(?P<pk>[0-9]+)/$', bookmark_detail, name='bookmark-detail'),
#     url(r'^users/$', user_list, name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
# ])


# version_6.2: Using ViewSets & Routers
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()

router.register(r'bookmarks', views.BookmarkViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
