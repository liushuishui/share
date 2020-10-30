# -*- coding: utf-8 -*-
# -----------------------------------
# 小程序的token
# -----------------------------------
import time
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from django.db import models
from .wxapp_config import WxAppConfig


class WxAppToken(models.Model):
    _transient_max_hours = 24

    class Meta:
        verbose_name = 'Token'
        verbose_name_plural = 'Token'

    token = models.CharField(
        max_length=500,
        db_index=True,
        verbose_name='token',
        blank=True
    )
    session_key = models.CharField(
        max_length=100,
        verbose_name='session_key',
        blank=True
    )
    openId = models.CharField(
        max_length=100,
        verbose_name='OpenID'
    )
    unionId = models.CharField(
        max_length=100,
        verbose_name='UnionID'
    )

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        super(WxAppToken, self).save(*args, **kwargs)

    @classmethod
    def generate_token(cls, unionId):
        config = WxAppConfig.objects.all()
        if config:
            config = config[0]
        else:
            raise
        secret_key = config.get_config('secret')
        app_id = config.get_config('app_id')
        if not secret_key or not app_id:
            raise
        s = Serializer(secret_key=secret_key, salt=app_id, expires_in=WxAppToken._transient_max_hours * 3600)
        timestamp = time.time()
        return s.dumps({'unionId': unionId, 'stamp': timestamp})
