# -*- coding: utf-8 -*-
# -----------------------------------
# 请输入该文件的说明
# -----------------------------------
from .mix_in import DefaultFieldMixIn
from django.db import models

GENDER = (
    (1, '男'),
    (0, '女'),
)


class WxAppUser(DefaultFieldMixIn):
    """小程序用户信息"""
    id = models.AutoField(
        primary_key=True
    )
    nickName = models.CharField(
        max_length=50,
        verbose_name='昵称'
    )
    openId = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name='OpenID'
    )
    unionId = models.CharField(
        max_length=100,
        db_index=True,
        verbose_name='UnionID'
    )
    gender = models.SmallIntegerField(
        choices=GENDER,
        verbose_name='性别'
    )
    language = models.CharField(
        max_length=10,
        verbose_name='语言',
        blank=True
    )
    phone = models.CharField(
        max_length=11,
        verbose_name='手机号',
        blank=True
    )
    country = models.CharField(
        max_length=30,
        verbose_name='国家',
        blank=True
    )
    province = models.CharField(
        max_length=30,
        verbose_name='省份',
        blank=True
    )
    city = models.CharField(
        max_length=30,
        verbose_name='城市',
        blank=True
    )
    avatarUrl = models.CharField(
        max_length=200,
        verbose_name='头像URL',
        blank=True
    )

    def __str__(self):
        return self.nickName

    class Meta:
        verbose_name = '小程序用户'
        verbose_name_plural = '小程序用户'

    def save(self, *args, **kwargs):
        user_info = WxAppUser.objects.filter(
            unionId=self.unionId
        )
        if user_info:
            self.delete()
        super(WxAppUser, self).save(*args, **kwargs)
