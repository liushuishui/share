# -*- coding:utf-8 -*-
# -------------------------------------
# 测试代码
# -------------------------------------
from multiprocessing import Pool
import requests
import json


class SeverPressureTest:
    def get_in(self):
        api = 'http://127.0.0.1:8000/user/register'
        data = {
            "encryptedData": "exz9KBamkgV38uBvFbAxkFfKURYTmWeQkH8EyktgEC0L4iwkwV85Wv58my8ZV2usCjDWYXljOqq/s0hcZxoxUQu/CCzvHXCQN2aeTXxkeweicSOLUXrZ6TqLU+5XFoLQz/drxGS0RwNTzpekQ3nVvvjPgGwKeGhyVXFnmGtmRZ2qkEHUOHJhjin+JJtKhU8+zHqssuU/pjlxsd+NvaDVsxv6czQtDWFYgWXCgdjlNpbA3URPiuDQMfSJuXp6LvQVlCJf6lKWRO3bSOuqnWyTqUdknJh4krlj0P+6ojpgAhEtyu42RD8Yh93f5gmmloU0u9PR5v8BU4zGLn8Hpy4oARKOGiKkplyHzPcOx1lxFgFaaiiLnYafKYKyzwhZmn0jVjd2S77EAI42T6/whE5N4pEZno/cTKDn60+HocyIJiQpF/zc1M41kLzqegTzxAlZkLPghv23PloDGD0O9SPkvNfK1g87POjE72hzb+VAEAvoRtqDIsd+k4BmP4xhu0IffnCXwrjhrCI31nZKHvQb7w==",
            "iv": "72K4B+jC6roAv/cJsOHZXQ==",
            "code": "023SJotJ0yRY1b25dYqJ0AzptJ0SJotU"
        }

        res = requests.post(
            api,
            json=data
        ).content.decode()

        print(res)
        print(type(res))

    def tasks(self):
        pool = Pool(10)
        # pool.apply(func=self.get_in)
        pool.apply_async(func=self.get_in)
        # pool.apply_async(func=self.get_in)
        # pool.apply_async(func=self.get_in)
        # pool.apply_async(func=self.get_in)
        # pool.apply_async(func=self.get_in)
        # pool.apply_async(func=self.get_in)
        # pool.apply_async(func=self.get_in)
        # pool.apply_async(func=self.get_in)
        # pool.apply_async(func=self.get_in)
        # pool.apply_async(func=self.get_in)
        pool.close()
        pool.join()


# if __name__ == "__main__":
#     testss = SeverPressureTest()
#     from pprint import pprint
#     pprint(testss.get_in())
#     for i in range(10):
#         print('--- turn number: %s' % i)
#         testss.tasks()

# testss = SeverPressureTest()
# testss.get_in()
sxs = {"code":"033vZM4F1yiEI40jcd3F11eR4F1vZM4T"}
sad = {'session_key': 'kMhf8BXr650Oo3XGUQfw8w==', 'openid': 'oP5C-4nakF4afS0YHy61Sm153ph8', 'unionid': 'oaYjxwFKUrEhFp0LoluUUOdPSyMA'}

data = 'mG+9jHVBKoRSD8n5l0/KWw7NLeP093Mpc2EuNkL2EZt2l5RaOS+ReME9O6v9T10CkMSPLGN1DTuUo6KjH1QAoWdy0wxMVuRrDmPNXvc9NfK88Fdl5Bw1GTWtGVsU8bIRn5bg64iR1cKnix7yhpG7hUdsSpsRj4FgiWwzwJUwWP8Bim98sv2pQyxI87+48doriGQ+BglAytIzbgByqACb7w=='
iv = 'jqe+gpWkJlXUxrTiIQKWyg=='
session_key = '8ZY+ZQw3/JQxFTCTWctuJg=='
app_id = 'wx5f4f5fee214350be'
from duck.oldcarshop.user.views.tools import get_decrypt_info
if __name__ == '__main__':
    print(get_decrypt_info(app_id, session_key, data, iv))



