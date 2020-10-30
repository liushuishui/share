# -*- coding: utf-8 -*-
# -----------------------------------
# 用户相关
# -----------------------------------
from ..models.wxapp_users import WxAppUser
from ..models.wxapp_config import WxAppConfig
from ..models.wxapp_token import WxAppToken
from .tools import get_wx_session_info, get_wx_user_info, get_decrypt_info
from .weixin.oauth2 import OAuth2AuthExchangeError
from common.base_view import BaseView

import logging

_logger = logging.getLogger(__name__)


class UserViews(BaseView):
    def register(self, request):
        """
        注册接口
        method == POST
        :param request: django的request对象
            :body 隐藏在请求体内的参数
                :code 前台传回的js_code，服务端与微信端换取用户信息
                :encryptedData 前台传回的加密数据
                :iv 前台传回的解密钥匙
        :return: 自定义token
        """
        try:
            # ret, entry = self._check_domain(sub_domain)
            # if ret: return ret
            # print(request.method)
            res = self.limit_request_method(
                request=request,
                method='POST'
            )
            if res:
                return self.res_err(errcode=res, code=405)
            # body = json.loads(request.body.decode())
            # code = body.get('code')
            # encrypted_data = body.get('encryptedData')
            # iv = body.get('iv')
            code = request.POST.get('code')
            encrypted_data = request.POST.get('encryptedData')
            iv = request.POST.get('iv')
            body = {
                'code': code,
                'encryptedData': encrypted_data,
                'iv': iv
            }

            if not code or not iv or not encrypted_data:
                return self.res_err(300)

            config = WxAppConfig.objects.all()
            if not config:
                return self.res_err(404)
            else:
                config = config[0]

            app_id = config.get_config('app_id')
            secret = config.get_config('secret')

            if not app_id or not secret:
                return self.res_err(404)
            body.update(
                {
                    'app_id': app_id,
                    'secret': secret
                }
            )
            # session_key, user_info = get_wx_user_info(app_id, secret, code, encrypted_data, iv)
            try:
                session_key, user_info = get_wx_user_info(**body)
            except OAuth2AuthExchangeError as e:
                return self.res_err(-1)
            is_exists = WxAppUser.objects.filter(
                unionId=user_info.get('unionId')
            )
            # 不存在该用户
            if not is_exists:
                user_info.pop('watermark')
                is_exists = WxAppUser(**user_info)
                is_exists.save()
            else:
                is_exists = is_exists[0]
            try:
                token = WxAppToken.objects.get(
                    unionId=user_info.get('unionId')
                )
            except Exception:
                token = None
            if not token:
                new_token = WxAppToken.generate_token(
                    unionId=user_info.get('unionId')
                )

                token_instance = WxAppToken(
                    openId=user_info.get('openId'),
                    unionId=user_info.get('unionId'),
                    token=new_token,
                    session_key=session_key
                )
                token_instance.save()
                data = {
                    'token': new_token
                }
            else:
                token.session_key = session_key
                token.save()
                data = {
                    'token': token.token
                }
            base = {
                'base': {
                    'mobile': is_exists.phone or '',
                    'userid': '',
                    'avatar': is_exists.avatarUrl or '',
                    'nickname': is_exists.nickName or '',
                },
            }
            data.update(
                {
                    'info': base
                }
            )
            return self.res_ok(data)
        except Exception as e:
            _logger.error(str(e))
            return self.res_err(-1, str(e))

    def login(self, request):
        """
        登陆接口
        method == POST
        :param request: django的request对象
            :body 隐藏在请求体内的参数
                :code 前台传回的js_code
        :return:  token
        """
        try:
            # ret, entry = self._check_domain(sub_domain)
            # if ret:return ret
            res = self.limit_request_method(
                request=request,
                method='POST'
            )
            if res:
                return self.res_err(errcode=res, code=405)

            # body = json.loads(request.body.decode())
            # code = body.get('code')
            code = request.POST.get('code')
            if not code:
                return self.res_err(300)

            # 获取小程序配置信息
            config = WxAppConfig.objects.all()
            if config:
                config = config[0]
            else:
                return self.res_err(300)

            app_id = config.get_config('app_id')
            secret = config.get_config('secret')
            if not app_id or not secret:
                return self.res_err(404)

            # 换取session_info
            session_info = get_wx_session_info(app_id, secret, code)
            if session_info.get('errcode'):
                return self.res_err(-1, session_info.get('errmsg'))

            unionId = session_info.get('unionid')
            openId = session_info.get('openid')

            wxapp_user = WxAppUser.objects.filter(unionId=unionId)[0]
            if not wxapp_user:
                return self.res_err(10000)
            try:
                token = WxAppToken.objects.get(unionId=unionId)
            except Exception:
                token = None
            # 判断是否有token
            if not token:
                new_token = WxAppToken.generate_token(
                    unionId=unionId
                )
                token = WxAppToken(
                    openId=openId,
                    unionId=unionId,
                    token=new_token,
                    session_key=session_info.get('session_key')
                )
                token.save()
                data = {
                    'token': new_token
                }
            else:
                token.session_key = session_info.get('session_key')
                token.save()
                data = {
                    'token': token.token
                }
            base = {
                'base': {
                    'mobile': wxapp_user.phone or '',
                    'userid': '',
                    'avatar': wxapp_user.avatarUrl or '',
                    'nickname': wxapp_user.nickName or '',
                },
            }
            data.update(
                {
                    'info': base
                }
            )
            return self.res_ok(data)

        except Exception as e:
            _logger.error(str(e))
            return self.res_err(-1, str(e))

    def phone(self, request):
        # try:
        # ret, entry = self._check_domain(sub_domain)
        # if ret: return ret
        res = self.limit_request_method(
            request=request,
            method='POST'
        )
        if res:
            return self.res_err(errcode=res, code=405)
        token = request.POST.get('token')
        encrypted_data = request.POST.get('encryptedData')
        iv = request.POST.get('iv')
        if not encrypted_data or not iv:
            return self.res_err(300)

        config = WxAppConfig.objects.all()
        if not config:
            return self.res_err(404)
        else:
            config = config[0]
        app_id = config.get_config('app_id')
        secret = config.get_config('secret')

        if not app_id or not secret:
            return self.res_err(404)

        access_token = WxAppToken.objects.filter(
            token=token
        )
        if not access_token:
            return self.res_err(4001)
        session_key = access_token[0].session_key
        user_info = get_decrypt_info(
            app_id, session_key,
            encrypted_data, iv
        )
        try:
            wxapp_user = WxAppUser.objects.get(
                unionId=access_token[0].unionId
            )
        except Exception:
            wxapp_user = None
        if wxapp_user:
            wxapp_user.phone = user_info.get('phoneNumber')
            wxapp_user.save()

        data = {
            'phone': user_info.get('phoneNumber', ''),
        }
        return self.res_ok(data)

        # except Exception as e:
        #     return self.res_err(-1)


class TestViews(BaseView):
    def testss(self, request):
        token = WxAppToken.objects.all().first()
        print(token.token)
        print(type(token.token))
        return self.res_ok()
