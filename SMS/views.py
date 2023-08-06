from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from .decorators import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from demoapi.serializers import StudentSerializer

# Create your views here.

def view_html(request):
    if request.method=='GET':
        resp=render(request,'SMS/file1.html')
        return resp
    elif request.method=='POST':
        pass


def view_modelfrm(request):
    if request.method=='GET':
        frm_bound=StudentForm()
        dict={"forms":frm_bound}
        resp=render(request,'SMS/file1.html',context=dict)
        return resp
    
    elif request.method=='POST':
        frm_unbound=StudentForm(request.POST,request.FILES)
        if frm_unbound.is_valid():
            frm_unbound.save()
            resp=HttpResponse('<h1>response stored successfully!!!</h1>')
            return resp
        else:
            dict={"frm_unbound":forms}
            resp=render(request,'SMS/file1.html',context=dict)
            return resp
        

def view_frmdet(request,sid):
        stu=Student.objects.get(id=sid)
        dict={"stu":stu}
        resp=render(request,'SMS/media.html',context=dict)
        return resp


def view_home(request):
    resp=render(request,'SMS/home.html')
    return resp

@func_Auth
def view_register(request):
    if request.method=='GET':
        frm_bound=UserCreationForm()
        dict={"forms":frm_bound}
        resp=render(request,'SMS/register.html',context=dict)
        return resp
    elif request.method=='POST':
        frm_unbound=UserCreationForm(request.POST)
        if frm_unbound.is_valid():
            u=frm_unbound.save()
            u.is_staff=True
            u.save()
            gr=Group.objects.get(id=1)
            u.groups.add(gr)

            resp=HttpResponse('<h1>Response stored successfully</h1>')
            return resp
        else:
            dict={"forms":frm_unbound}
            resp=render(request,'SMS/register.html',context=dict)
            return resp
        


@func_Auth
def view_login(request):
    if request.method=='GET':
        resp=render(request,'SMS/login.html')
        return resp
    elif request.method=='POST':
        u1=request.POST.get('t1','N.A')
        u2=request.POST.get('p1','N.A')
        u=authenticate(request=request,username=u1,password=u2)
        if u is not None:
            login(request,user=u)
            resp=render(request,'SMS/home.html')
            return resp
        else:
            resp=render(request,'SMS/login.html')
            return resp
        

def view_logout(request):
    logout(request=request)
    resp=render(request,'SMS/logout.html')
    return resp

@login_required(login_url='login')
def view_secure1(request):
    resp=render(request,'SMS/secure1.html')
    return resp

@login_required(login_url='login')
def view_secure2(request):
    resp=render(request,'SMS/secure2.html')
    return resp



def view_unsecure1(request):
    resp=render(request,'SMS/unsecure1.html')
    return resp

def view_unsecure2(request):
    resp=render(request,'SMS/unsecure2.html')
    return resp

@api_view(['GET'])
def api_get(request,sid):
    stu=Student.objects.get(id=sid)
    serial=StudentSerializer(stu)
    resp=Response(data=serial.data)
    return resp

@api_view(['POST'])
def api_post(request):
    serial=StudentSerializer(data=request.data)
    if serial.is_valid():
        serial.save()
        resp=Response(serial.data)
        return resp
    else:
        resp=Response(data="not found")
        return resp


    



