from django.contrib import admin
from django.urls import path
from .views import listfunc ,Create ,detailfunc ,mypagefunc ,loginfunc ,signupfunc

urlpatterns = [
    path('list/',listfunc,name='list'),
    path('create/',Create.as_view(),name='create'),
    path('detail/<int:pk>',detailfunc,name='detail'),
    path('mypage/',mypagefunc,name='mypage'),
    path('login/',loginfunc,name='login'),
    path('signup/',signupfunc,name='signup'),
]