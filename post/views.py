from math import ceil

from django.core.cache import cache
from django.shortcuts import render, redirect

from post.models import Post


def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(title=title, content=content)
        return redirect('/post/read/?post_id=%d' % post.id)
    else:
        return render(request, 'create_post.html')


def edit_post(request):
    if request.method == 'POST':
        post_id = int(request.POST.get('post_id'))
        post = Post.objects.get(pk=post_id)

        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()

        # 更新帖子缓存
        key = 'Post-%s' % post_id
        cache.set(key, post)

        return redirect('/post/read/?post_id=%d' % post_id)
    else:
        post_id = request.GET.get('post_id')
        post = Post.objects.get(pk=post_id)
    return render(request, 'edit_post.html', {'post': post})

    #     return redirect('/post/read/?post_id=%d'% post.id)
    # else:
    #     return render(request, 'create_post.html')


def read_post(request):
    post_id = int(request.GET.get('post_id'))

    key = 'Post-%s' % post_id
    post = cache.get(key)
    print('从缓存获取：',post)
    if post is None:
        post = Post.objects.get(pk=post_id)
        cache.set(key, post)
        print('从数据库获取：',post)
    return render(request, 'read_post.html', {'post': post})


def delete_post(request):
    post_id = int(request.GET.get('post_id'))
    Post.objects.get(pk=post_id).delete()
    return redirect('/')


def post_list(request):
    page = int(request.GET.get('page', 1))
    total = Post.objects.count()  # 文章总数
    per_page = 10  # 每页数
    pages = ceil(total / per_page)  # 总页数

    start = (page - 1) * per_page
    end = start + per_page
    posts = Post.objects.filter()[start:end]

    return render(request, 'post_list.html', {'posts': posts,'pages':range(pages)})


def search(request):
    keyword = request.POST.get('keyword')
    posts = Post.objects.filter(title__contains=keyword)
    return render(request, 'search.html', {'posts': posts})
