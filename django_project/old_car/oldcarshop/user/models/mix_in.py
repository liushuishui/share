# -*- coding: utf-8 -*-
# -----------------------------------
# 共有字段的mix-in
# -----------------------------------
from django.db import models


class DefaultFieldMixIn(models.Model):
    create_on = models.DateTimeField(
        verbose_name='创建时间',
        auto_now_add=True
    )
    last_update = models.DateTimeField(
        verbose_name='上次修改时间',
        auto_now=True
    )

    class Meta:
        abstract = True
