from django.contrib import admin
from django.urls import path,include
from base import views

from django.http import JsonResponse

urlpatterns = [

    path('', views.index,name="basepage"),
    path('ownerpage/',views.owner,name="owner"),
    #path('gmc/',views.gmc,name="gmc"),
    path('endpoint/', views.endpoint_view, name='endpoint'),
    path('experiments/', views.experiment, name='experiment'),
    path('signin/', views.signin, name='signin'),
    path('listbuliding/', views.listbuilding, name='listbuilding'),
    path('index2/', views.index2, name='index2'),
    path('getcoordinates/', views.getcoordinates, name='getcoordinates'),
    path('notify/', views.notify, name='notify'),
    path('customer/', views.customer, name='customer')

    

    
    

]
