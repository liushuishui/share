 - 如果psycopg2报错，就先行安装libpq-dev
 ```bash
sudo apt-get install libpq-dev
# 或者
sudo apt-get install python3-dev
```
- 如果报错 No module named "Crypto"，就到虚拟环境里将crypto文件名更改为Crypto
- 如果更改之后再报错 No module named ‘Crypto.Cipher’，需要执行两个命令
```bash
# 1. 卸载pycrypto模块
pip3 uninstall pycrypto
# 2. 安装pycryptodome模块
pip3 install pycryptodome
```
