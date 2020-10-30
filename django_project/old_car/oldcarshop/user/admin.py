from django.contrib import admin
from .models.wxapp_token import WxAppToken
from .models.wxapp_config import WxAppConfig
from .models.wxapp_users import WxAppUser

admin.site.register(WxAppUser)
admin.site.register(WxAppToken)
admin.site.register(WxAppConfig)
