from django.shortcuts import render


def func_Auth(myfunc):
    def inner(request):
        if request.user.is_authenticated:
            return render(request,'SMS/home.html')
        else:
            return myfunc(request)
    return inner