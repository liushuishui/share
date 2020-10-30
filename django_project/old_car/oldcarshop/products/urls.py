# -*- coding: utf-8 -*-
# -----------------------------------
# 请输入该文件的说明
# -----------------------------------
from django.urls import path
from .views.testss import TestView
from .views.product_info import ShowProduct

urlpatterns = [
    path('imgtest', TestView().get_image_test),
    path('meta', TestView().get_meta),
    path('data', TestView().many_test),
    path('cate', ShowProduct().show_cate),
    path('detail', ShowProduct().show_product),
    path('brand', ShowProduct().show_brand),
    path('slide', ShowProduct().show_slide),
]
