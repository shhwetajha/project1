from django.urls import path
from.views import *
#http://127.0.0.1:8000/dm/

urlpatterns=[

path('dp/', api_func),
path('mp/<int:sid>/',model_api),
path('aj/',view_ajax),
path('sess/',view_session),
path('cookwr/',view_cookwr),
path('cookrd/',view_cookrd)
]