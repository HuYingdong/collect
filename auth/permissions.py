from rest_framework.permissions import BasePermission


class Userpermission(BasePermission):

    message = '你没有权限~'

    SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
    CREATE_METHODS = ('POST', 'PUT')
    DELETE_METHODS = ('DELETE',)
    ALL_METHODS = CREATE_METHODS + DELETE_METHODS

    def has_permission(self, request, view):

        if request.query_params.get('table') == 'userinfo':
            return False

        # 只读
        if request.method in self.SAFE_METHODS:
            return True
        # 读、写、改
        elif request.method in self.CREATE_METHODS and request.user.user_type in (2, 4):
            return True
        # 读、删
        elif request.method in self.DELETE_METHODS and request.user.user_type in (3, 4):
            return True
        else:
            return False
