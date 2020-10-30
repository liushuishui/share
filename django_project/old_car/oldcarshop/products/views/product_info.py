# -*- coding:utf-8 -*-
# -------------------------------------
# 商品信息
# -------------------------------------
from common.base_view import BaseView, NEW_OLD
from ..models.pro_info import ProCategory, ProBrand, ProImage, ProDetail
from ..models.first_page_config import FirstPageSlide


class ShowProduct(BaseView):
    def object_to_dict(self, _object, db_name):
        res = super(ShowProduct, self).object_to_dict(_object, db_name)
        new_old = res.get('new_old')
        if db_name == 'products.prodetail':
            res.update(
                {
                    'new_old_cn': NEW_OLD.get(new_old)
                }
            )
        return res

    def show_cate(self, request):
        """
        获取产品分类的接口
        :param request:
            :-> pid: 指定的父级分类id
        :return: 分类的具体值，如果不传pid则返回所有顶级分类
        """
        res = self.limit_request_method(
            request=request,
            method='POST'
        )
        if res:
            return self.res_err(errcode=res, code=405)
        pid = request.POST.get('pid')
        # token = request.POST.get('token')
        # if not token:
        #     return self.res_err(4001)
        # wxapp_user = self.check_user(token)
        # if not wxapp_user:
        #     return self.res_err(4001)
        cate_info = ProCategory.objects.filter(
            parent_id=pid
        )
        res = self.operate_each_objects(
            cate_info, 'products.procategory'
        )
        return self.res_ok(data=res)

    def show_product(self, request):
        """
        展示某分类下的商品
        :param request:
            -> cate_id: 分类的id
            -> product_id: 产品id
            -> page: 页码
            -> size: 每页条数
        :return: 商品详情
        """
        try:
            res = self.limit_request_method(
                request=request,
                method='POST'
            )
            if res:
                return self.res_err(errcode=res, code=405)
            cate_id = request.POST.get('cate_id')
            product_id = request.POST.get('product_id')
            is_recommend = request.POST.get('is_recommend')
            mark = request.POST.get('mark')
            # token = request.POST.get('token')
            # if not token:
            #     return self.res_err(4001)
            # wxapp_user = self.check_user(token)
            # if not wxapp_user:
            #     return self.res_err(4001)
            # 情景1：点击分类时
            if mark == 'CATE':
                if not cate_id:
                    return self.res_err(4002)
                product_info = ProDetail.objects.filter(
                    category_id=cate_id,
                    sale_status='sell',
                    is_on_sale='on'
                )
            # 情景2：点击进入商品详情时
            elif mark == 'DETAIL':
                if not product_id:
                    return self.res_err(4002)
                product_info = ProDetail.objects.filter(
                    id=product_id,
                    sale_status='sell',
                    is_on_sale='on'
                )
            elif mark == 'RECO':
                if not is_recommend:
                    return self.res_err(4002)
                product_info = ProDetail.objects.filter(
                    sale_status='sell',
                    is_recommend=is_recommend
                )
            # 情景3：默认商品列表时
            elif mark == 'LIST':
                product_info = ProDetail.objects.all()
            else:
                return self.res_err(4002)
            if not product_info:
                return self.res_err(4004)
            size = int(request.GET.get('size', 20))
            page = int(request.GET.get('page', 1))
            if mark == 'RECO':
                size = int(request.GET.get('size', 2))
                page = int(request.GET.get('page', 1))
            product_info = self.pager(
                pg=page,
                size=size,
                record=product_info
            )
            # 将QuerySet对象转换为字典对象
            res = self.operate_each_objects(
                product_info, 'products.prodetail'
            )
            target = {
                'brand': ['name'],
                'category': ['id', 'name']
            }
            # 将字典对象内的外键转换为指定的值
            new = self.foreign_main(res, target)
            from django.conf import settings
            # pprint(new)
            # res = product_info[0]
            # pprint(dir(res))
            # pprint(dir(res.images.model))
            # print(res.images.model)
            # cate_id = product_info[0].brand
            # stock = product_info[0].stock
            # print(res.instance)
            # cate_id = getattr(product_info[0], 'images')
            #
            #
            # pprint(dir(cate_id))
            # print(cate_id)
            # print(hasattr(cate_id, 'instance'))
            # print(cate_id.__class__)
            # print(stock.__class__)
            # print(res.db)
            # print(res.model)
            # print(res.model.model_name)
            # pprint(request.META)
            # print(request)
            # print(request.get_host())
            return self.res_ok(new)
        except Exception:
            return self.res_err(errcode=-1, code=404)

    def show_brand(self, request):
        """
        展示产品的品牌信息
        根据品牌筛选产品
        :param request:
            -> brand_id: 产品的品牌id
            -> size: 每页数据量
            -> page: 页码
        :return:
        """
        try:
            res = self.limit_request_method(
                request=request,
                method='POST'
            )
            if res:
                return self.res_err(errcode=res, code=405)
            brand_id = request.POST.get('brand_id')
            # token = request.POST.get('token')
            # if not token:
            #     return self.res_err(4001)
            # wxapp_user = self.check_user(token)
            # if not wxapp_user:
            #     return self.res_err(4001)
            if brand_id:
                product_info = ProDetail.objects.filter(
                    brand_id=brand_id,
                    sale_status='sell',
                    is_on_sale='on'
                )
                size = int(request.POST.get('size', 1))
                page = int(request.POST.get('page', 20))

                product_info = self.pager(
                    pg=page,
                    size=size,
                    record=product_info
                )
                # 将QuerySet对象转换为字典对象
                res = self.operate_each_objects(
                    product_info, 'products.prodetail'
                )
                target = {
                    'brand': ['name'],
                    'category': ['id', 'name']
                }
                # 将字典对象内的外键转换为指定的值
                new = self.foreign_main(res, target)
                return self.res_ok(new)
            else:
                brand_info = ProBrand.objects.all()
                res = self.operate_each_objects(
                    brand_info, 'products.probrand'
                )
                return self.res_ok(res)
        except Exception:
            return self.res_err(errcode=-1, code=404)

    def show_slide(self, request):
        res = self.limit_request_method(
            request=request,
            method='POST'
        )
        if res:
            return self.res_err(errcode=res, code=405)

        slide_info = FirstPageSlide.objects.filter(
            is_show='on',
        )
        res = self.operate_each_objects(
            slide_info, 'products.first.page.slide'
        )
        target = {
            'product': ['id'],
        }
        # 将字典对象内的外键转换为指定的值
        new = self.foreign_main(res, target)
        return self.res_ok(new)



