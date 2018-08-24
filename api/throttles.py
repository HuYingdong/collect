# coding=utf-8

from rest_framework.throttling import SimpleRateThrottle


class VisitThrottle(SimpleRateThrottle):

    scope = 'ip'

    def get_cache_key(self, request, view):
        return self.get_ident(request)


class UserThrottle(SimpleRateThrottle):

    scope = 'user'

    def get_cache_key(self, request, view):
        return request.user.username


# VISIT_RECORD = {}
# class VisitThrottle(object):
#     import time
#     def __init__(self):
#         self.history = None
#
#     def allow_request(self, request, view):
#         # 获取用户IP
#         remote_addr = request.META.get('REMOTE_ADDR')
#         ctime = time.time()
#         if remote_addr not in VISIT_RECORD:
#             VISIT_RECORD[remote_addr] = [ctime]
#             return True
#
#         history = VISIT_RECORD.get(remote_addr)
#         self.history = history
#
#         while history and history[-1] < ctime - 60:
#             history.pop()
#
#         if len(history) < 3:
#             history.insert(0, ctime)
#             return True
#
#     def wait(self):
#         """
#         还需要等待的时间
#         """
#         ctime = time.time()
#         return 60 - (ctime-self.history[-1])
