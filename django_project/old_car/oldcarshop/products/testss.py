# -*- coding: utf-8 -*-
# -----------------------------------
# 请输入该文件的说明
# -----------------------------------
import json

axa = {
    "params":{
        "encryptedData":"3PfoD8d2buG4wmk8gX1Ol+XkZI0SvQshOdFqEyHU2btakP7Un6Y3QZ2nFzpSaS18NxfqGa03zdf7/lbFuDepUNq35REQva2APQpqb/7fReg5/5BVojiryucChBBvnHf4J2zZ8ocXsUHtiYO2fGa7ZlvKbnn775GVxbE9snTUj4DOAXiX7prKqL6wNibDT/g3AmHfgbI/vY6V5Vf17ixZ+y69XX8e+49mhfI0LapeHJd/6TAKJlbeZVa8DpouQae+G0WaTFk1DNc9rJmRo9W0FMRLWQiaN/skCcCmLqx8/Uas7JW36spHfc210mvkwqNaS20uFAPyVhY9SC5F5dDjGBtn9ktCnqNElqi8Scy7tSGUh/69dWS+laPYeQ8xnmFbHwuSXb45y41u+MajRDIB8q5u9790+zRit5QWz4APWqr6byvGQAtMvFJPfVNLKgMPy1g50uiK6KNgdpadJ2XbUtwZO/MJCkBmSeK9Jv31ufI0DNABOo/GkEyxweb9bkTIvRYL5GlbykX7Z5AO6dWtVg==",
        "iv":"NjRwGwFfUozMeHev6mkcag==",
        "code":"033HTevh2atjTC0Kjuwh26bjvh2HTevv"
    }
}
aca = {
    "encryptedData":"N9qwhtw/SmcC0SVEXWmnr9Y44zjmBAQGalEWD7LRQhjbS9u7EB1rt9KKbK3ax4rRKv2yIbCEbJmpJ0FRyGIXztt+oo4usy/b5MNZANRmUvTkvhSJP8c+HTTVSACvEc4XOfvAsvssJB8uOicBuixjQgTduRBwq6wL8KmMMjR7MIQFkp9iHTqaUpM6EhnykirY42o+NcKDxB3ixEk5SOJmH6I+WwZO4PuK4CY57Gw8XhlRKEyaAc6TfMjZ1bV4MXLQxbN0HVjB+Y68e/aKckgPYF2+JIdpbZHaVz13vs6NDkYqfOBDqf04SVEjAtecKV17L5vN9skrBzkiErYl84mfOy6HMVBQvVizYTuR9hpus3zBpR7CGiMEDsJvE8HpGVk6iLCmrpZvsUTrvwIoHN0dxr52BN+vxKe0cCtg5rMjA813VNzsGoU8CqBOS2G0Jxj6hTa+Rc5Dvwx10uoO5PE1LanqqOJPBC6Tutch56a6d2stJ3nnMoqOsn5LmEwFFG2WxddkIbXykQrExcBs4zSE4w==",
    "iv":"ptY7INz2mH0JyxRBLSxJXA==",
    "code":"043lae5z1unhVc0AiY8z1Nji5z1lae5s"
}

# getUserInfo
"""
{
    "code": 0,
    "msg": "success",
    "data": {
        "session_key": "1waJGEUUnEsVhdGIjuU+2w==",
        "user_info": {
            "openId": "oP5C-4nakF4afS0YHy61Sm153ph8",
            "nickName": "Yes？",
            "gender": 1,
            "language": "zh_CN",
            "city": "Shijiazhuang",
            "province": "Hebei",
            "country": "China",
            "avatarUrl": "https://wx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTIsdRrBgLQXC7RhEgJ2VV6huu27mIF8LBWhj6OW46Iqga9JAgeUyG3xUOh6V9LodbxauafUDgfMiag/132",
            "unionId": "oaYjxwFKUrEhFp0LoluUUOdPSyMA",
            "watermark": {
                "timestamp": 1591347639,
                "appid": "wx5f4f5fee214350be"
            }
        }
    }
}"""


def func(**kw):
    print(kw)
    print(kw.get('name'))


dic = {
    'name': 'cc',
    'age': '20',
    'gender': 'nan',
}

# print(list(dic.keys()))
# print(dic.values())
# for i in dic.keys():
#     print(i)

trt = 'cate_id'
# print(trt.endswith('_id'))
import os
from urllib import parse
from nturl2path import pathname2url


base_dir = 'D:\django_work\duck\oldcarshop\image'
image_url = '/image/%E5%85%AB%E7%AD%89.jpg'
image_url = parse.unquote(image_url)
# aaa = pathname2url(base_dir)
# print(aaa)
os.path.split(base_dir)
ress = os.path.join(base_dir, os.path.split(image_url)[1])
print(ress)

receipt_type = [
    ('purchase', '购物小票'),
    ('return', '退货小票'),
]

# receipt_type = fields.Char(string='小票种类',help="purchase和return")
kw = {
    "params": {
        "access_token":"MTU5MjIyMjA5Mi41NzIxMDE6MzczOWY3YzYyY2Q3NjI4NGExMzNlNTNiZjVlMmQ5NTk5ODE5YzgyOA==",
        'promotion_amount': 0,
        'discount': 0,
        'payee': '2014',

        'product_data': [
            {
                'product_type': '99020104',
                'mall_field': '0003020101',
                'origin_receipt_no': None,
                'row_no': 1,
                'list_price': 17.9,
                'tran_flag': '4',
                'temp_discount': 0,
                'specs_no': '00',
                'final_price': 17.9,
                'sold_price': 17.9,
                'price': 17.9,
                'origin_casher_no': '',
                'pro_discount': 0,
                'code': '407891',
                'quantity': 1,
                'salesman': '商场',
                'code_type': '1',
                'member_discount': 0,
                'barcode': '6901894153053',
                'product_brand': '00203',
                'name': '白猫激光驱蚊杀虫剂茉莉香型'
            },
            {
                'product_type': '99020104',
                'mall_field': '0003020101',
                'origin_receipt_no': None,
                'row_no': 2,
                'list_price': 17.9,
                'tran_flag': '4',
                'temp_discount': 0,
                'specs_no': '00',
                'final_price': 17.9,
                'sold_price': 17.9,
                'price': 17.9,
                'origin_casher_no': '',
                'pro_discount': 0,
                'code': '407891',
                'quantity': 1,
                'salesman': '商>场',
                'code_type': '1',
                'member_discount': 0,
                'barcode': '6901894153053',
                'product_brand': '00203',
                'name': '白猫激光驱蚊杀虫剂茉莉香型'
            },
            {
                'product_type': '99020104',
                'mall_field': '0003020101',
                'origin_receipt_no': None,
                'row_no': 3,
                'list_price': 17.9,
                'tran_flag': '4',
                'temp_discount': 0,
                'specs_no': '00',
                'final_price': 17.9,
                'sold_price': 17.9,
                'price': 17.9,
                'origin_casher_no': '',
                'pro_discount': 0,
                'code': '407891',
                'quantity': 1,
                'salesman': '商场',
                'code_type': '1',
                'member_discount': 0,
                'barcode': '6901894153053',
                'product_brand': '00203',
                'name': '白猫激光驱蚊杀虫剂茉莉香型'
            }
        ],
        'total_amount': 53.7,
        'company': '正定瑞天超市华安店',
        'compute_bonus_flag': False,

        'member_discount': 0,
        'phone': '13035883464',

        'quantity': 3,
        'shop': '正定瑞天超市华安店',
        'datetime': '2020-04-24 12:00:35',
        'actual_pay': 53.7,
        'amount': 53.7,
        'pay_data': [
            {'pay_no': '', 'code': '现金', 'amount': 53.7, 'origin_pay_no': ''}
        ],
        'casher': '3009',
        'change': 0,
        'receipt_no': '2004240055',
        'transaction_no': '11527',
        'shop_no': '0007',
        'receipt_type': 'return',
    }
}
# import json
# print(json.dumps(kw))

# {"params": {"access_token": "MTU5MjIyMjA5Mi41NzIxMDE6MzczOWY3YzYyY2Q3NjI4NGExMzNlNTNiZjVlMmQ5NTk5ODE5YzgyOA==", "promotion_amount": 0, "discount": 0, "payee": "2014", "product_data": [{"product_type": "99020104", "mall_field": "0003020101", "origin_receipt_no": null, "row_no": 1, "list_price": 17.9, "tran_flag": "4", "temp_discount": 0, "specs_no": "00", "final_price": 17.9, "sold_price": 17.9, "price": 17.9, "origin_casher_no": "", "pro_discount": 0, "code": "407891", "quantity": 1, "salesman": "\u5546\u573a", "code_type": "1", "member_discount": 0, "barcode": "6901894153053", "product_brand": "00203", "name": "\u767d\u732b\u6fc0\u5149\u9a71\u868a\u6740\u866b\u5242\u8309\u8389\u9999\u578b"}, {"product_type": "99020104", "mall_field": "0003020101", "origin_receipt_no": null, "row_no": 2, "list_price": 17.9, "tran_flag": "4", "temp_discount": 0, "specs_no": "00", "final_price": 17.9, "sold_price": 17.9, "price": 17.9, "origin_casher_no": "", "pro_discount": 0, "code": "407891", "quantity": 1, "salesman": "\u5546>\u573a", "code_type": "1", "member_discount": 0, "barcode": "6901894153053", "product_brand": "00203", "name": "\u767d\u732b\u6fc0\u5149\u9a71\u868a\u6740\u866b\u5242\u8309\u8389\u9999\u578b"}, {"product_type": "99020104", "mall_field": "0003020101", "origin_receipt_no": null, "row_no": 3, "list_price": 17.9, "tran_flag": "4", "temp_discount": 0, "specs_no": "00", "final_price": 17.9, "sold_price": 17.9, "price": 17.9, "origin_casher_no": "", "pro_discount": 0, "code": "407891", "quantity": 1, "salesman": "\u5546\u573a", "code_type": "1", "member_discount": 0, "barcode": "6901894153053", "product_brand": "00203", "name": "\u767d\u732b\u6fc0\u5149\u9a71\u868a\u6740\u866b\u5242\u8309\u8389\u9999\u578b"}], "total_amount": 53.7, "company": "\u6b63\u5b9a\u745e\u5929\u8d85\u5e02\u534e\u5b89\u5e97", "compute_bonus_flag": false, "member_discount": 0, "phone": "13035883464", "quantity": 3, "shop": "\u6b63\u5b9a\u745e\u5929\u8d85\u5e02\u534e\u5b89\u5e97", "datetime": "2020-04-24 12:00:35", "actual_pay": 53.7, "amount": 53.7, "pay_data": [{"pay_no": "", "code": "\u73b0\u91d1", "amount": 53.7, "origin_pay_no": ""}], "casher": "3009", "change": 0, "receipt_no": "2004240055", "transaction_no": "11527", "shop_no": "0007", "receipt_type": "return"}}

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
import time
def generate_token(unionId):

    secret_key = 'fdc255b37b728b391268a5684fe60096'
    app_id = 'wx5f4f5fee214350be'
    if not secret_key or not app_id:
        raise
    s = Serializer(secret_key=secret_key, salt=app_id, expires_in=3600)
    timestamp = time.time()
    return s.dumps({'unionId': unionId, 'stamp': timestamp})

union = 'oaYjxwFKUrEhFp0LoluUUOdPSyMA'

awa = generate_token(union)
print(awa)
print(type(awa))
