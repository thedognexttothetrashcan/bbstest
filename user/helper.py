from django.shortcuts import redirect


def login_required(view_fun):
    def check(request):
        if 'uid' in request.session:
            return view_fun(request)
        else:
            return redirect('/user/login/')
    return check