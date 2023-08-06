from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from SMS.models import Student
from .serializers import StudentSerializer


# Create your views here.
@api_view(['GET'])
def api_func(request):
    resp=Response(data='This is my first view')
    return resp

@api_view(['GET','POST'])
def model_api(request,sid):
    stu=Student.objects.get(id=sid)
    serial=StudentSerializer(stu)
    resp=Response(data=serial.data)
    return resp


def view_ajax(request):
    resp=render(request,'demoapi/js.html')
    return resp


def view_session(request):
    if request.method=='GET':
        resp=render(request,'demoapi/session.html')
        return resp
    elif request.method=='POST':
        count=request.session.get('count','N.A')
        if count=='N.A':
            count=1
        else:
            count+=1
        request.session['count']=count
        dict={'count':count}
        resp=render(request,'demoapi/session.html',context=dict)
        return resp


def view_cookwr(request):
    if request.method=='GET':
        resp=render(request,'demoapi/cookiwr.html')
        return resp
    elif request.method=='POST':
        name=request.POST.get('co1','N.A')
        resp=render(request,'demoapi/cookiwr.html')
        resp.set_cookie(key='name',value=name)
        return resp


def view_cookrd(request):
    if request.method=='GET':
        resp=render(request,'demoapi/cookrd.html')
        return resp
    elif request.method=='POST':
        name=request.COOKIES.get('name','N.A')
        if name=='N.A':
            data='cookies not found'
        else:
            data=name
        dict={"data":data}
        resp=render(request,'demoapi/cookrd.html',context=dict)
        return resp
    
