# -*- coding: utf-8 -*-
# -----------------------------------
# 请输入该文件的说明
# -----------------------------------
from django.http.response import JsonResponse
from django.http import response
from common.base_view import BaseView
from ..models.pro_info import ProImage, ProDetail
import sys


class TestView(BaseView):
    def get_image_test(self, request):
        img = ProImage.objects.all()
        print(img)
        test_num = 56665
        if img:
            for i in img:
                print(i)
                print('file--', i.image.file)
                print('image--', i.image)
                print('image url', i.image.url)
                print('image size', i.image.size)
                print('image path', i.image.path)
                # print(i.image.open().read())
                print('size of image', sys.getsizeof(i.image))
                print('size of test', sys.getsizeof(test_num))
        return self.res_ok()

    def get_meta(self, request):
        from pprint import pprint
        # pprint(request.META)
        # cookie = request.COOKIES
        response = JsonResponse(
            {
                'code': 0,
                'msg': 'seccess'
            }
        )
        # response.set_cookie(key='name', value='lisa')
        # request.set_cookie(key='name', value='lisa')
        print(request.COOKIES)
        return response

    def many_test(self, request):

        detail = ProDetail.objects.all()
        if detail:
            detail = detail[0]
        else:
            return self.res_err(404)
        data = {
            'name': detail.name,
            'category': detail.category.name,
            'brand': detail.brand.name,
            'images': [rec.image.url for rec in detail.images.all()],
        }
        return self.res_ok(data=data)
