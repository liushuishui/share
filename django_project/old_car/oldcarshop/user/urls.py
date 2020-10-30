# -*- coding: utf-8 -*-
# -----------------------------------
# 请输入该文件的说明
# -----------------------------------
from django.urls import path
from .views.users import UserViews, TestViews


urlpatterns = [
    path('login', UserViews().login),
    path('register', UserViews().register),
    path('phone', UserViews().phone),
    path('test', TestViews().testss),
]