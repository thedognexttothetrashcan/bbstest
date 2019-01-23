from django.shortcuts import redirect, render

from user.models import User


def login_required(view_fun):
    def check(request):
        if 'uid' in request.session:
            return view_fun(request)
        else:
            return redirect('/user/login/')
    return check


def need_prem(perm_nmae):
    def deco(view_func):
        def wrapper(request):
            user = User.objects.get(pk=request.session['uid'])
            if user.has_prem(perm_nmae):
                return view_func(request)
            else:
                return render(request, 'blockers.html')
        return wrapper
    return deco



