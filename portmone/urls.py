# -*- coding: utf-8 -*-
try:
    from django.conf.urls import url
except ImportError:
    from django.urls import re_path as url
from portmone import views

urlpatterns = [
    url(r'^result/$', views.authorize_result, name='portmone-result'),
    url(r'^success/$', views.success, name='portmone-success'),
    url(r'^fail/$', views.fail, name='portmone-fail'),
]
