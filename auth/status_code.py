import functools
import logging

from rest_framework.response import Response
from .exceptions import OrderException, InvalidPolicyID, CustomerException, \
    TembinException, FengShenException, APINotRegisterError, RequestsError

logger = logging.getLogger('auth.views')
# 返回值定义
STATUS = 'status'
MESSAGE = 'message'
RESULT = 'result'
MODULE = 'module'
MODULE_NAME = 'auth'

# 返回状态码定义，以status开头
STATUS_SUCCESS = 2000

STATUS_PARAM_NULL = 4000
STATUS_PARAM_ILLEGAL = 4001

STATUS_DB_ERROR = 4002
STATUS_DB_MULTI = 4003
STATUS_DB_NOT_FOUND = 4004

STATUS_AAA_REQUEST = 4005
STATUS_MOVE_ERROR = 4006
STATUS_REQUEST_ERROR = 4007
STATUS_INVALID_POLICY_ID = 4008
STATUS_NO_CUS_PERMISSION = 4009
STATUS_NO_SERV_PERMISSION = 4010
STATUS_FACTORY_ERROR = 4011

STATUS_REQUEST_THIRD_API_ERROR = 6000
STATUS_ORDER_API_ERROR = 6001
STATUS_HIGOS_API_ERROR = 6002
STATUS_TEMBIN_API_ERROR = 6003
STATUS_FENGSHEN_API_ERROR = 6004
STATUS_NOT_REGISTER_API_ERROR = 6005

# 返回消息定义，以message开头
MESSAGE_SUCCESS = 'success'

MESSAGE_PARAM_NULL = '%s is null'
MESSAGE_PARAM_ILLEGAL = '%s is illegal'

MESSAGE_DB_ERROR = 'operate db occur error'
MESSAGE_DB_MULTI = 'object is already exists'
MESSAGE_DB_NOT_FOUND = 'the object can not be found with the id %s.'
MESSAGE_INVALID_POLICY_ID = 'invalid policy id'

MESSAGE_AAA_REQUEST = 'request aaa error'
MESSAGE_MOVE_ERROR = 'move policy error'
MESSAGE_REQUEST_ERROR = 'request api error'
MESSAGE_REQUEST_THIRD_API_ERROR = 'request third api error'
MESSAGE_FACTORY_ERROR = 'factory import error'

MSG_CODE = {
    STATUS_NO_CUS_PERMISSION: 'The account does not have the customer permission',
    STATUS_NO_SERV_PERMISSION: 'The account does not have the service permission'
}


def success(result={}):
    return Response({
        STATUS: STATUS_SUCCESS,
        MESSAGE: MESSAGE_SUCCESS,
        RESULT: result,
        MODULE: MODULE_NAME
    })


def service_offline():
    return Response({
        STATUS: 4444,
        MESSAGE: "service offline yet",
        RESULT: None,
        MODULE: MODULE_NAME
    })


def params_null(message, result=None):
    return Response({
        STATUS: STATUS_PARAM_NULL,
        MESSAGE: message,
        RESULT: result,
        MODULE: MODULE_NAME
    })


def params_illegal(message, result=None):
    return Response({
        STATUS: STATUS_PARAM_ILLEGAL,
        MESSAGE: message,
        RESULT: result,
        MODULE: MODULE_NAME
    })


def db_error(message=MESSAGE_DB_ERROR, result=None):
    return Response({
        STATUS: STATUS_DB_ERROR,
        MESSAGE: message,
        RESULT: result,
        MODULE: MODULE_NAME
    })


def db_not_found(message, result=None):
    return Response({
        STATUS: STATUS_DB_NOT_FOUND,
        MESSAGE: MESSAGE_DB_NOT_FOUND % message,
        RESULT: result,
        MODULE: MODULE_NAME
    })


def db_multi(message=MESSAGE_DB_MULTI, result=None):
    return Response({
        STATUS: STATUS_DB_MULTI,
        MESSAGE: message,
        RESULT: result,
        MODULE: MODULE_NAME
    })


def aaa_error(message=MESSAGE_AAA_REQUEST, result=None):
    return Response({
        STATUS: STATUS_AAA_REQUEST,
        MESSAGE: message,
        RESULT: result,
        MODULE: MODULE_NAME
    })


def move_error(message=MESSAGE_MOVE_ERROR, result=None):
    return Response({
        STATUS: STATUS_MOVE_ERROR,
        MESSAGE: message,
        RESULT: result,
        MODULE: MODULE_NAME
    })


def request_error(message=MESSAGE_REQUEST_ERROR, result=None):
    return Response({
        STATUS: STATUS_REQUEST_ERROR,
        MESSAGE: message,
        RESULT: result,
        MODULE: MODULE_NAME
    })


def request_factory_error(message=MESSAGE_FACTORY_ERROR, result=None):
    return Response({
        STATUS: STATUS_FACTORY_ERROR,
        MESSAGE: message,
        RESULT: result,
        MODULE: MODULE_NAME
    })


def request_update_use_count_error(message="", status=2000, result=None):
    return Response({
        STATUS: status,
        MESSAGE: message,
        RESULT: result,
        MODULE: MODULE_NAME
    })


def handle_exception(func):
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except RequestsError as ex:
            logger.error('request api exception status: %s, message: %s',
                         ex.code, ex)
            return Response({
                STATUS: STATUS_REQUEST_THIRD_API_ERROR,
                MESSAGE: MESSAGE_REQUEST_THIRD_API_ERROR,
                RESULT: '',
                MODULE: MODULE_NAME
            })
        except OrderException as ex:
            logger.error('order api exception status: %s, message: %s',
                         ex.code, ex)
            return Response({
                STATUS: STATUS_ORDER_API_ERROR,
                MESSAGE: ex,
                MODULE: ex.module,
                RESULT: ex.result
            })
        except APINotRegisterError as ex:
            logger.error('api not register status: %s, message: %s',
                         ex.code, ex)
            return Response({
                STATUS: STATUS_NOT_REGISTER_API_ERROR,
                MESSAGE: ex,
                MODULE: ex.module,
                RESULT: ex.result
            })
        except InvalidPolicyID as ex:
            logger.error('invalid policy id')
            return Response({
                STATUS: STATUS_INVALID_POLICY_ID,
                MESSAGE: MESSAGE_INVALID_POLICY_ID,
                MODULE: MODULE_NAME,
                RESULT: ''
            })
        except CustomerException as ex:
            logger.error('higos api exception status: %s, message: %s',
                         ex.code, ex)
            return Response({
                STATUS: STATUS_HIGOS_API_ERROR,
                MESSAGE: ex,
                MODULE: ex.module,
                RESULT: ex.result
            })
        except TembinException as ex:
            logger.error('tembin api exception status: %s, message: %s',
                         ex.code, ex)
            return Response({
                STATUS: STATUS_TEMBIN_API_ERROR,
                MESSAGE: ex,
                MODULE: ex.module,
                RESULT: ex.result
            })
        except FengShenException as ex:
            logger.error('fengshen api exception status: %s, message: %s',
                         ex.code, ex)
            return Response({
                STATUS: STATUS_FENGSHEN_API_ERROR,
                MESSAGE: ex,
                MODULE: ex.module,
                RESULT: ex.result
            })
    return decorator


def response_func(result=None, status=STATUS_SUCCESS, message=None, module=MODULE_NAME):
    if message is None:
        message = MSG_CODE[status]
    return Response({
        STATUS: status,
        MODULE: module,
        MESSAGE: message,
        RESULT: result
    })
