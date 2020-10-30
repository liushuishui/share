# -*- coding:utf-8 -*-
# -------------------------------------
# 请输入该文件的说明
# -------------------------------------
from django.db import models
from .mix_in import DefaultFieldMixIn


IS_SHOW = [
    ('on', '展示'),
    ('off', '隐藏'),
]


class FirstPageSlide(DefaultFieldMixIn):
    model_name = 'products.first.page.slide'

    class Meta:
        verbose_name = '首页幻灯配置'
        verbose_name_plural = '首页幻灯配置'

    name = models.CharField(
        max_length=10,
        verbose_name='名称'
    )
    element = models.ImageField(
        verbose_name='幻灯图片',
        blank=True,
        null=True
    )
    is_show = models.CharField(
        verbose_name='是否展示',
        choices=IS_SHOW,
        max_length=3,
        default='on'
    )
    product = models.ForeignKey(
        'ProDetail',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='链接商品'
    )

    def __str__(self):
        return self.name
