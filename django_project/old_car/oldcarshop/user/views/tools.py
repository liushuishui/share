# -*- coding: utf-8 -*-
# -----------------------------------
# 请输入该文件的说明
# -----------------------------------

# -*- coding: utf-8 -*-

from .weixin.lib.wxcrypt import WXBizDataCrypt
from .weixin import WXAPPAPI
from .weixin.oauth2 import OAuth2AuthExchangeError


def get_wx_session_info(app_id, secret, code):
    api = WXAPPAPI(appid=app_id, app_secret=secret)
    try:
        session_info = api.exchange_code_for_session_key(code=code)
    except OAuth2AuthExchangeError as e:
        raise e
    return session_info


def get_wx_user_info(app_id, secret, code, encryptedData, iv):
    session_info = get_wx_session_info(app_id, secret, code)
    session_key = session_info.get('session_key')
    crypt = WXBizDataCrypt(app_id, session_key)
    user_info = crypt.decrypt(encryptedData, iv)
    return session_key, user_info


def get_decrypt_info(app_id, session_key, encrypted_data, iv):
    crypt = WXBizDataCrypt(app_id, session_key)
    _info = crypt.decrypt(encrypted_data, iv)
    return _info

