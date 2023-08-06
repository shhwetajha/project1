from django.urls import path
from .views import *
#http://127.0.0.1:8000/sms/
urlpatterns=[

    path('html/',view_html),
    path('frm/', view_modelfrm),
    path('med/<int:sid>/',view_frmdet),
    path('home/',view_home,name='home'),
    path('login/',view_login,name='login'),
    path('logout/',view_logout,name='logout'),
    path('register/',view_register,name='register'),
    path('secure1/',view_secure1,name='secure1'),
    path('secure2/',view_secure2,name='secure2'),
    path('unsecure1/',view_unsecure1,name='unsecure1'),
    path('unsecure2/',view_unsecure2,name='unsecure2'),
    path('apiget/<int:sid>/',api_get),
    path('apipost/',api_post)
    



]