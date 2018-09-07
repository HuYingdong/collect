from auth.models import UserToken
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication


class UserAuthentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.query_params.get('token')
        token_obj = UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed('用户认证失败')
        # 在rest_framework 内部会将这两个字段赋值给request，以供后续操作使用
        return token_obj.user, token_obj

    def authenticate_header(self, request):
        return 'Basic realm=auth'
