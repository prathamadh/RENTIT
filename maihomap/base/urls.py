from django.contrib import admin
from django.urls import path,include
from base import views

from django.http import JsonResponse

urlpatterns = [

    path('', views.index,name="basepage"),
    path('ownerpage/',views.owner,name="owner"),
    #path('gmc/',views.gmc,name="gmc"),
    path('endpoint/', views.endpoint_view, name='endpoint')
]
