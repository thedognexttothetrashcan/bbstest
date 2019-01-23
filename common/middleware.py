import time

from django.core.cache import cache
from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin


def test_middleware(view_func):
    def wrapper(request):
        print('1.view执行之前的处理')
        response = view_func(request)
        print('2.view执行之后的处理')
        return response
    return wrapper

#
# class BlockMilddleware(MiddlewareMixin):
#     def process_request(self,request):
#         user_ip = request.META['REMOTE_ADDR']
#         request_key = 'Request-%s' % user_ip
#
#         black_key = 'Block-%s' % user_ip
#
#         if cache.has_key(black_key):
#             return render(request,'blockers.html')
#
#         now = time.time()
#         # 检查当前时间与前三次的是啊金是否小于1秒
#         request_time = cache.get(request_key,[0]*3)
#         if now - request_time[0]<1:
#             # TODO 封禁IP
#
#             cache.set(black_key, 1, 10)
#             return render(request,'blockers.html')
#         else:
#             request_time.pop()
#             request_time.append(now)
#             cache.set(request_key, request_time)
class BlockMiddleware(MiddlewareMixin):
    def process_request(self, request):
        user_ip = request.META['REMOTE_ADDR']
        request_key = 'Request-%s' % user_ip
        block_key = 'Block-%s' % user_ip
        # print(request_key,'*'*100)

        # 黑名单检查
        if cache.has_key(block_key):
            return render(request, 'blockers.html')

        now = time.time()
        # 检查当前时间与前三次的时差是否 小于 1 秒
        request_time = cache.get(request_key, [0] * 10)
        if now - request_time[0] < 3:
            # 封禁 IP
            cache.set(block_key, 1, 5)
            return render(request, 'blockers.html')
        else:
            # 更新访问时间
            request_time.pop(0)
            request_time.append(now)
            cache.set(request_key, request_time)
