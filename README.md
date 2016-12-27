## 启动方式

```
mysql.server start
source venv/bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py runserver

```
## 如果需要在手机端访问开发机器的代码，运行下面的命令，但同时需要在fmit/settings.py里面添加ip地址

```
./manage.py runserver 0.0.0.0:8000

```

## 创建超级管理员

```
./manage.py createsuperuser

```

## 管理员功能页面地址：

* 127.0.0.1:8000/admin
