# -*- coding: utf-8 -*-
# -----------------------------------
# 公共视图
# -----------------------------------
from django.http import JsonResponse
from user.models.wxapp_token import WxAppToken
from user.models.wxapp_config import WxAppConfig

error_code = {
    -1: '服务器繁忙，请稍后重试',
    0: 'success',
    #
    4001: 'token认证失败',
    4002: '缺少参数',
    4004: '数据不存在',
}

NEW_OLD = {
    '10': '十成新',
    '09': '九成新',
    '08': '八成新',
    '07': '七成新',
    '06': '六成新',
    '05': '五成新',
    '04': '五成以下',
}

# =====================
# 需要返回字典的模型字段
# =====================
FIELD = {
    'products.procategory': [
        'id',
        'name',
        'parent_id'
    ],
    'products.prodetail': [
        'id',
        'name',
        'images',
        'category',
        'brand',
        'pro_model',
        'new_old',
        'fuel_type',
        'engine_model',
        'stock',
        'driver_seat',
        'engine_system',
        'original_use',
        'electric_system',
        'liquid_pressure_system',
        'outside_paint',
        'sale_status',
        'is_on_sale',
    ],
    'products.proimage': [
        'image'
    ],
    'products.probrand': [
        'id',
        'name',
        'made_in'
    ],
    'products.first.page.slide': [
        'element',
        'product'
    ]
}


class DataOperateProxy:
    # ==================
    # queryset转换为dict||
    # ==================
    def operate_each_objects(self, _objects, db_name):
        """
        将QuerySet对象处理成可加载成json的字典格式
        :param _objects: QuerySet对象
        :param db_name: 模型名，app.model_name
        :param target_fields: 目标字段
        :return: [{'field1': value1, ...}, ...]
        """
        res = list(
            map(
                lambda x: self.object_to_dict(x, db_name),
                _objects
            )
        )
        return res

    def object_to_dict(self, _object, db_name):
        """
        根据db_name获取到设定好的字段名数组，根据数组内的名字取到对象的值
        :param _object: QuerySet内的一个数据集
        :param db_name: 模型名，app.model_name
        :return: {'field1': value1, ...}
        """
        res = {key: self.operate_each_field(_object, key) for key in FIELD.get(db_name, [])}
        return res

    def operate_each_field(self, _object, each_field):
        value = getattr(_object, each_field)
        # 普通字段
        if isinstance(value, str) or isinstance(value, int):
            return value
        # foreignkey
        if hasattr(value, 'save') and hasattr(value, 'save_base'):
            return self.object_to_dict(value, value.model_name)
        # manytomany
        if hasattr(value, 'instance') and hasattr(value, 'through'):
            return self.operate_each_objects(value.all(), value.model.model_name)
        # image
        if hasattr(value, 'url') and hasattr(value, 'size'):
            config = WxAppConfig.objects.all()
            return config[0].custom_addr + value.url

    # =======================
    # foreignkey转换成指定字段||
    # =======================
    def foreign_main(self, rec, target):
        """
        将数据集内的外键字段的值进行处理，筛选出指定的值
        :param rec: <list> 需要处理的数据集，[{field1:val1, ...}, {{field1:val1, ...}]
        :param target: <dict> 字段名称及指定子字段 {name1: [id, name,..], name2: [id,], ...}
        :return: 处理好的数据集

        # 处理前的数据格式， brand与category是需要处理的外键字段
        # 指定的target如下：
            target = {
                'brand': ['name'],
                'category': ['id', 'name']
            }

        [{'brand': {'id': 1, 'made_in': '山东', 'name': '临工'},
          'category': {'id': 2, 'name': '铲车', 'parent_id': None},
          'driver_seat': '良好',
          'electric_system': '良好',
          'engine_model': 'YC6L330-55',
          'engine_system': '良好',
          'fuel_type': '0',
          'id': 1,
          'images': [{'image': '/image/%E5%85%AB%E7%AD%89.jpg'}],
          'liquid_pressure_system': '良好',
          'name': '我是谁',
          'new_old': '10',
          'original_use': '工地',
          'outside_paint': '良好',
          'pro_model': 'PRO',
          'stock': 1}]

        # 处理后的数据格式，将brand与category字段删除，替换成了category_id, category_name, brand_name
        [{'brand_name': '临工',
          'category_id': 2,
          'category_name': '铲车',
          'driver_seat': '良好',
          'electric_system': '良好',
          'engine_model': 'YC6L330-55',
          'engine_system': '良好',
          'fuel_type': '0',
          'id': 1,
          'images': [{'image': '/image/%E5%85%AB%E7%AD%89.jpg'}],
          'liquid_pressure_system': '良好',
          'name': '我是谁',
          'new_old': '10',
          'original_use': '工地',
          'outside_paint': '良好',
          'pro_model': 'PRO',
          'stock': 1}]
        """
        # 拆分出每一条数据
        res = list(
            map(
                lambda x: self.operate_foreign_fields(x, target),
                rec
            )
        )
        return res

    def operate_foreign_fields(self, each_rec, target):
        """
        将数据集内的单条数据取出，处理每条数据的外键
        :param each_rec: <dict> 单条数据, {field1: val1, field2: val2, ..}
        :param target: <dict> 字段名称及指定子字段 {name1: [id, name,..], name2: [id,], ...}
        :return: 处理好的单条数据
        """
        # 筛选出指定数据的指定字段
        target_name = list(target.keys())
        for name in target_name:
            self.operate_each_foreign(each_rec.get(name), target.get(name), name, each_rec)
        return each_rec

    def operate_each_foreign(self, each_foreign, target_keys, field_name, each_rec):
        """
        将每个外键进行特殊处理，提取出指定的字段，并将原来的外键字段删除，替换成新的字段
        :param each_foreign: <dict> 外键的值，
        :param target_keys: <list> 需要提取的指定值
        :param field_name: <str> 该外键的名字
        :param each_rec: <dict> 当前数据
        :return:
        """
        # 外键取出外键字段的指定值
        res = {'%s_%s' % (field_name, key): each_foreign.get(key) for key in target_keys}
        each_rec.pop(field_name)
        each_rec.update(res)


class PageProxy:
    def pager(self, pg=None, size=None, record=None):
        """
        将获取到的数据进行分页
        :param pg: 页码
        :param size: 每页所含数据条数
        :param record: 获取到的数据集合
        :return: 数据字典
        """
        pg = int(pg)
        size = int(size)
        # 整除取对应size的总页数
        page = len(record) // size
        # 如果存在余数，就将页数加1
        if len(record) % size:
            page = page + 1
        start_index = pg * size - size
        if pg > page:
            data = record[start_index:]
        else:
            end_index = pg * size
            data = record[start_index:end_index]
        return data


class BaseView(DataOperateProxy, PageProxy):
    def res_ok(self, data=None, code=200):
        ret = {
            'errcode': 0,
            'errmsg': error_code.get(0)
        }
        if data:
            ret.update({
                'data': data
            })
        # In order to allow non-dict objects to be serialized set the safe parameter to False
        # 将安全改为False，否则无法返回
        r = JsonResponse(ret, safe=False)
        if code != 200:
            r.status_code = code
        return r

    def res_err(self, errcode, data=None, code=200):
        ret = {
            'errcode': errcode,
            'errmsg': error_code.get(errcode)
        }
        if data:
            ret.update({
                'data': data
            })
        r = JsonResponse(ret, safe=False)
        if code != 200:
            r.status_code = code
        return r

    def limit_request_method(self, request=None, method=None):
        if request.method != method:
            return 405
        else:
            return None

    def check_user(self, token):
        try:
            is_exists = WxAppToken.objects.filter(
                token=token
            )
        except Exception:
            is_exists = None

        return is_exists
