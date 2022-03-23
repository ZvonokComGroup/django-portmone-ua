# -*- coding: utf-8 -*-
from django.urls import path
from portmone import views

urlpatterns = [
    path('result/', views.authorize_result, name='portmone-result'),
    path('success/', views.success, name='portmone-success'),
    path('fail/', views.fail, name='portmone-fail'),
]
