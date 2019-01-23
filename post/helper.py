from django.core.cache import cache

from common import rds
from post.models import Post


def page_cache(timeout):
    '''页面缓存'''

    def deco(view_func):
        def wrapper(request):
            # 定义缓存 Key
            session_id = request.session.session_key
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


def get_top_n(n):
    '''

    :param n: 前十
    :return:
    '''
    origin_data = rds.zrevrange('ReadCounter', 0, n - 1, withscores=True)
    cleaned_data = [[int(post_id), int(count)]
                    for post_id, count in origin_data]

    # for item in cleaned_data:
    #     post_id = item[0]
    #     post = Post.objects.get(pk=post_id)
    #     item[0] = post

    post_id_list = [post_id for post_id, _ in cleaned_data]
    post = Post.objects.filter(pk__in=post_id_list)
    post = sorted(post, key=lambda post:post_id_list.index(post.id))

    for item, post in zip(cleaned_data, post):
        item[0] = post

    # post_id_list = [post_id for post_id,_ in cleaned_data]
    # post = Post.objects.in_bulk(post_id_list)
    # # print(dir(Post.objects))
    # for item in cleaned_data:
    #     post_id = item[0]
    #     item[0] = post[post_id]

    return cleaned_data
