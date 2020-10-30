# -*- coding: utf-8 -*-
# -----------------------------------
# 请输入该文件的说明
# -----------------------------------
from django.db import models
from .mix_in import DefaultFieldMixIn

NEW_OLD = (
    ('10', '十成新'),
    ('09', '九成新'),
    ('08', '八成新'),
    ('07', '七成新'),
    ('06', '六成新'),
    ('05', '五成新'),
    ('04', '五成以下'),
)

FUEL = (
    ('0', '柴油'),
    ('1', '汽油')
)

PRO_STATUS = (
    ('sold', '已售'),
    ('sell', '未售'),
)

ON_SALE = (
    ('on', '上架'),
    ('off', '下架'),
)

RECOMMEND_PRO = (
    ('on', '推荐商品'),
    ('off', '普通商品'),
)


class ProCategory(DefaultFieldMixIn):
    model_name = 'products.procategory'

    class Meta:
        verbose_name = '产品分类'
        verbose_name_plural = '产品分类'

    name = models.CharField(
        max_length=15,
        verbose_name='分类名称'
    )
    parent = models.ForeignKey(
        'ProCategory',
        verbose_name='父级分类',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


class ProBrand(DefaultFieldMixIn):
    model_name = 'products.probrand'

    class Meta:
        verbose_name = '品牌'
        verbose_name_plural = '品牌'

    name = models.CharField(
        max_length=10,
        verbose_name='品牌名称'
    )
    made_in = models.CharField(
        max_length=100,
        verbose_name='产地'
    )

    def __str__(self):
        return self.name


class ProImage(DefaultFieldMixIn):
    model_name = 'products.proimage'

    class Meta:
        verbose_name = '商品图片'
        verbose_name_plural = '商品图片'
    name = models.CharField(
        verbose_name='图片名称',
        max_length=10,
        default=True
    )
    image = models.ImageField(
        verbose_name='图片',
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     from pprint import pprint
    #     from django.contrib import admin
    #     print('args--', args)
    #     print('kwargs--', kwargs)
    #     print('self', self)
    #     print('url', admin.site.urls)
    #     pprint(dir(self.Meta))
    #     super(ProImage, self).save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        """
        admin页面内删除图片时，静态文件内的图片跟着删除
        :param using:
        :param keep_parents:
        :return:
        """
        from django.conf import settings
        import os
        from urllib import parse
        base_dir = settings.MEDIA_ROOT
        image_url = self.image.url
        image_url = parse.unquote(image_url)
        abs_path = os.path.join(base_dir, os.path.split(image_url)[1])
        os.remove(abs_path)
        return super(ProImage, self).delete(using, keep_parents)


class ProDetail(DefaultFieldMixIn):
    model_name = 'products.prodetail'

    class Meta:
        verbose_name = '产品详情'
        verbose_name_plural = '产品详情'

    sale_status = models.CharField(
        max_length=4,
        verbose_name='商品状态',
        choices=PRO_STATUS,
        default='sell'
    )
    is_on_sale = models.CharField(
        max_length=3,
        verbose_name='是否上架',
        choices=ON_SALE,
        default='on'
    )
    is_recommend = models.CharField(
        max_length=3,
        verbose_name='是否设为推荐',
        choices=RECOMMEND_PRO,
        default='off'
    )
    name = models.CharField(
        max_length=50,
        verbose_name='产品名称'
    )
    images = models.ManyToManyField(
        ProImage,
        blank=True,
        # through='ProDetailImage',
        # related_name='细节照片',
        # on_delete=models.CASCADE,
        # verbose_name='细节照片',
    )
    category = models.ForeignKey(
        'ProCategory',
        on_delete=models.CASCADE,
        verbose_name='分类',
        default=True
    )
    brand = models.ForeignKey(
        'ProBrand',
        on_delete=models.CASCADE,
        verbose_name='品牌',
        default=True
    )
    pro_model = models.CharField(
        max_length=50,
        verbose_name='产品型号'
    )
    new_old = models.CharField(
        max_length=2,
        choices=NEW_OLD,
        verbose_name='成色'
    )
    fuel_type = models.CharField(
        max_length=1,
        choices=FUEL,
        verbose_name='燃油',
        default='0'
    )
    engine_model = models.CharField(
        max_length=30,
        verbose_name='发动机型号'
    )
    stock = models.IntegerField(
        verbose_name='库存',
        default=1
    )
    # ==================================
    # 车辆车况描述
    # ==================================
    driver_seat = models.CharField(
        max_length=100,
        verbose_name='驾驶室情况'
    )
    engine_system = models.CharField(
        max_length=100,
        verbose_name='动力系统情况'
    )
    original_use = models.CharField(
        max_length=100,
        verbose_name='原车用途'
    )
    electric_system = models.CharField(
        max_length=100,
        verbose_name='电气系统情况'
    )
    liquid_pressure_system = models.CharField(
        max_length=100,
        verbose_name='液压系统情况'
    )
    outside_paint = models.CharField(
        max_length=100,
        verbose_name='面漆情况'
    )
    # bool_test = models.BooleanField(
    #     verbose_name='布尔测试字段',
    #     default=True
    # )
    # tags = models.CharField(
    #     max_length=100,
    #     verbose_name='标签'
    # )

    def __str__(self):
        return self.name


# class ProDetailImage(DefaultFieldMixIn):
#     image = models.ForeignKey(
#         ProImage,
#         on_delete=models.CASCADE,
#         verbose_name='照片'
#     )
#
#     detail = models.ForeignKey(
#         ProDetail,
#         on_delete=models.CASCADE,
#         verbose_name='详情'
#     )






