from django.db import transaction, connection
from rest_framework.response import Response
from rest_framework.views import APIView
from auth import status_code
from auth.sql_utils import Mysql
from auth.status_code import handle_exception
from auth.models import UserInfo, UserToken
from .helper import md5
from auth.authtications import UserAuthentication
from auth.permissions import Userpermission
from auth.throttles import VisitThrottle, UserThrottle
import logging


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    level=logging.DEBUG, datefmt='%Y-%m-%d %X')
logger = logging.getLogger('auth.view')


class AuthView(APIView):
    """
    用户登录认证
    """
    throttle_classes = [VisitThrottle, ]
    # authentication_classes = [UserAuthentication, ]
    # permission_classes = [Userpermission, ]

    def get(self, request, *args, **kwargs):
        ret = {'code': 1000, 'msg': None}
        return Response(ret)

    def post(self, request, *args, **kwargs):
        ret = {'code': 1000, 'msg': None}
        try:
            user = request.data.get('username')
            pwd = request.data.get('password')
            ret['msg'] = '请输入用户名' if not user else '请输入密码' if not pwd else 'both'
            if ret['msg'] != 'both':
                ret['code'] = 1001
                return Response(ret)

            obj = UserInfo.objects.filter(username=user, password=pwd).first()
            if not obj:
                ret['code'] = 1002
                ret['msg'] = '用户名或密码错误'
                return Response(ret)

            # 为登录用户创建token
            token = md5(user)
            # 存在就更新，不存在就创建
            UserToken.objects.update_or_create(user=obj, defaults={'token': token})
            ret['token'] = token
            # request.session['user_token'] = token
        except Exception as e:
            ret['code'] = 1002
            ret['msg'] = '请求异常'
            import traceback
            traceback.print_exc()
            logger.exception('error')

        return Response(ret)


class NotifyView(APIView):

    authentication_classes = [UserAuthentication, ]
    permission_classes = [Userpermission, ]
    throttle_classes = [UserThrottle, ]

    @staticmethod
    @handle_exception
    def get(request):
        """
            select
        """
        print('user', request.user, request.auth)

        req_data = request.query_params.dict()
        table = req_data.get('table')
        values = req_data.get('values')
        cond = req_data.get('cond')
        # 查询数据库
        with transaction.atomic():
            with connection.cursor() as cursor:
                try:
                    result = Mysql.select(table, values, cond, cursor)
                    return status_code.success(result)
                except Exception as e:
                    import traceback
                    traceback.print_exc()
                    print('error:%s' % e)
                    return status_code.db_error(e)

    @staticmethod
    @handle_exception
    def post(request):
        """
            insert
        """
        req_data = request.data
        table = req_data.get('table')
        values = req_data.get('values')

        print('req_data', req_data)
        print(table, values)

        # 添加数据库
        with transaction.atomic():
            with connection.cursor() as cursor:
                try:
                    result = Mysql.insert(table, values, cursor)
                    print('result', result)
                    return status_code.success(result)
                except Exception as e:
                    import traceback
                    traceback.print_exc()
                    print('error:%s' % e)
                    return status_code.db_error(e)

    @staticmethod
    @handle_exception
    def put(request):
        """
            update
        """
        req_data = request.data
        table = req_data.get('table')
        values = req_data.get('values')
        cond = req_data.get('cond')
        print('req_data', req_data)
        print(table, values, cond)
        # 更新数据库
        with transaction.atomic():
            with connection.cursor() as cursor:
                try:
                    result = Mysql.update(table, values, cond, cursor)
                    print('result', result)
                    return status_code.success(result)
                except Exception as e:
                    import traceback
                    traceback.print_exc()
                    print('error:%s' % e)
                    return status_code.db_error(e)

    @staticmethod
    @handle_exception
    def delete(request):
        """
            delete
        """
        req_data = request.data
        print('req_data', req_data)
        table = req_data.get('table')
        cond = req_data.get('cond')
        print(table, cond)

        # 删除数据
        with transaction.atomic():
            with connection.cursor() as cursor:
                try:
                    result = Mysql.delete(table, cond, cursor)
                    print('result', result)
                    return status_code.success(result)
                except Exception as e:
                    import traceback
                    traceback.print_exc()
                    print('error:%s' % e)
                    return status_code.db_error(e)
