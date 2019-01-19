from django.core.cache import cache

def page_cache(timeout):
    '''页面缓存'''
    def deco(view_func):
        def wrapper(request):
            # 定义缓存 Key
            session_id = request.session  .session_key
            url = request.get_full_path()
            key = 'PageCache-%s-%s' % (session_id, url)

            # 从缓存获取 Response
            response = cache.get(key)
            print(request.get_full_path())
            print('get from cache:', response)
            if response is None:
                # 执行 View 函数，并将 response 加入缓存
                response = view_func(request)
                cache.set(key, response, timeout)
                print('get from view:', response)
            return response
        return wrapper
    return deco




