# 如何启动工程

安装依赖（使用python3的pip，非python2）

```
pip install Django pymysql sqlalchemy
```

（可能不全，如果运行起来报错就按照报错安装相应的pip模块，没有版本限制）

首先跳转到工程根目录，然后执行：

```
python manage.py runserver
```

默认在8000端口上运行，如果你想修改端口号：

```
python manage.py runserver 端口号
```

运行起来后，用浏览器访问

```
localhost:8000
```

即可看到测试页面。（在测试数据库前，请先按照demo.sql配置好本地MySQL数据库）

### 注：这只是一个Django示例工程，帮助你们熟悉Django框架。请不要将项目的代码推送到这个仓库。

### 真正的项目代码仓库我之后会创建。

# 工程结构介绍

```
test_django/
├── db.sqlite3
├── demo.sql
├── manage.py
├── page_changer
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── README.md
├── static
│   ├── css
│   │   └── test.css
│   └── js
│       └── jquery-3.4.1.js
├── templates
│   └── test.html
├── testbackend
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   └── views.py
└── test_django
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## /manage.py

根目录中的`manage.py`是启动器与管理器。启动方法前文已经介绍。

## app folders

这个demo有两个apps: ```page_changer```和```testbackend```

其中```page_changer```负责页面的跳转，```testbackend```负责后端业务逻辑。

可以看到，这两个apps的内部目录结构是完全一样的。

## app

在一个app目录中，唯一需要编辑的是```views.py```，你需要在这里面编写你的业务逻辑。

这个文件中所定义的函数将被```test_django/urls.py```调用。

我已经在```page_changer/views.py```中提供了页面跳转的示例，在```testbackend/views.py```中提供了接收post请求或get请求并返回响应的示例，以及连接数据库执行SQL语句的示例。

数据库的表结构在```demo.sql```中。使用sql之前不要忘记在本地MySQL创建数据库、创建表。

## /test_django/

``test_django``目录中存放本工程相关的一些文件。

其中，```test_django/urls.py```相当于映射表，将请求的路径映射到某个app中的某个函数上。因此在创建app后，不要忘记在这个文件中import这个新的app，以便于调用里面的函数。

```test_django/settings.py```中存放本工程的一些配置。在这个文件中，唯一需要你修改的地方就是创建新的app之后，需要在这里注册一下：

```
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "testbackend",
    "page_changer",
]
```

## /templates/

这里面存放写好的html页面。html中可以正常使用JavaScript或jQuery。Django工程会直接集成这些页面，无需另行部署apache服务器。

## /static/

将图片或者js文件存放于此。在html文件中使用Django模板语言引入。

# 如何创建新的app

首先，跳转到工程根目录并执行以下命令：

```
python manage.py startapp app名称
```

这样该app的目录将被创建。

随后修改```test_django/urls.py```，import这个新的app，修改```test_django/settings.py```注册这个新的app。
