"""MobileApplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from .views import create_brand,delete_brand,brand_update,mobile_create,list_mobile,detail_mobile,user_register,user_login,user_logout,product_order,cart_items,errorpage

urlpatterns = [
    path('errorpage',errorpage,name="errorpage"),
    path("",lambda request:render(request,'mobile/index.html')),
    path('create',create_brand,name="create"),
    path('delete/<int:id>',delete_brand,name="delete"),
    path('update/<int:id>',brand_update,name="update"),
    path('mobiles',mobile_create,name="createmobile"),
    path('mobile/list',list_mobile,name="listmobiles"),
    path('mobile/detail/<int:id>',detail_mobile,name="detail"),
    path('mobile/userregistration',user_register,name="userregistration"),
    path('mobile/userlogin',user_login,name="userlogin"),
    path('mobile/userlogout',user_logout,name="userlogout"),
    path('mobile/order',product_order,name="order"),
    path('mobile/cart',cart_items,name="cart"),




]
