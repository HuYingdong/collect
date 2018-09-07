# !/usr/bin/env python
# -*- coding: utf-8 -*-


class RegisterServiceErr(Exception):
    pass


class RequestMethodErr(Exception):
    pass


class AAARequestsError(Exception):
    pass


class MovePolicyError(Exception):
    pass


class NoticeRequestsError(Exception):
    pass


class EventRequestsError(Exception):
    pass


class APINotRegisterError(Exception):
    def __init__(self, code, message, module=None, result=None):
        self.code = code
        self.module = module
        self.result = result
        super(APINotRegisterError, self).__init__(message)


class DuplicatePolicy(Exception):
    pass


class InvalidPolicyID(Exception):
    pass


class OrderException(Exception):
    def __init__(self, code, message, module=None, result=None):
        self.code = code
        self.module = module
        self.result = result
        super(OrderException, self).__init__(message)


class CustomerException(Exception):
    def __init__(self, code, message, module=None, result=None):
        self.code = code
        self.module = module
        self.result = result
        super(CustomerException, self).__init__(message)


class TembinException(Exception):
    def __init__(self, code, message, module=None, result=None):
        self.code = code
        self.module = module
        self.result = result
        super(TembinException, self).__init__(message)


class FengShenException(Exception):
    def __init__(self, code, message, module=None, result=None):
        self.code = code
        self.module = module
        self.result = result
        super(FengShenException, self).__init__(message)


class InvalidParametersException(Exception):
    pass


class RequestsError(Exception):
    def __init__(self, code=None, message=None):
        self.code = code
        super(RequestsError, self).__init__(message)


class DBParamError(Exception):
    pass


class DBOpError(Exception):
    pass


class DBObjNotExist(Exception):
    pass


class DBMultiError(Exception):
    pass
