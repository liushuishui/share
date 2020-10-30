# -*- coding: utf-8 -*-
# -----------------------------------
# 小程序设置
# -----------------------------------
from django.db import models
from .mix_in import DefaultFieldMixIn


class WxAppConfig(DefaultFieldMixIn):
    class Meta:
        verbose_name = '小程序配置信息'
        verbose_name_plural = '小程序配置信息'

    mall_name = models.CharField(
        max_length=10,
        verbose_name='商户名称'
    )
    app_id = models.CharField(
        max_length=200,
        verbose_name='小程序AppID',

    )
    secret = models.CharField(
        max_length=200,
        verbose_name='小程序Secret',
    )
    mch_id = models.CharField(
        max_length=200,
        verbose_name='商户号',
        null=True,
        blank=True,
    )
    mch_key = models.CharField(
        max_length=200,
        verbose_name='商户密钥',
        null=True,
        blank=True,
    )
    custom_addr = models.CharField(
        max_length=50,
        verbose_name='服务器域名',
        blank=True
    )

    def __str__(self):
        return self.mall_name

    def get_config(self, key):
        res = WxAppConfig.objects.all()
        if not res:
            return None
        return self.__getattribute__(key)
    # cert_id = models.FileField
    # cert_id = fields.Binary('CA证书文件(.pem)', attachment=True)
    # cert_key = fields.Binary('CA密钥文件(.pem)', attachment=True)
