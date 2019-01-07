# 第２章　django入门


#　安装django=1.10.3

#  2.2.1  创建项目与应用

#  django-admin.py startproject guest

#　__init__.py:一个空的文件，用它标识一个目录为python的标准包
# settings.py:django的项目的配置文件，包括django的模块应用配置，数据库配置，模板配置等
# urls.py:django项目的url声明
# wsgi.py: 与WSGI兼容的web服务器为你的项目服务的入口点
#  manage.py:一个命令行工具，可以让你在使用django项目时以不同的方式进行交互

#　startapp命令创建应用．一个项目可以包含多个应用，而我们要开发的签到系统需要在具体应用下完成

# 创建应用　python manage.py startapp sign

#　migrations/:  用于记录models中数据的变更
#　 admin.py:映射models中数据到django自带的admin后台
#　apps.py:用于应用程序的配置，在新的django版本中新增文件
#　models.py:django的模型文件，创建应用程序数据表模型(对应数据库的相关操作)
# tests.py : 创建django测试用例

#　views.py:django的视图文件，控制向前端显示的内容


# 应用创建后，别忘了，一定要在settings.py中注册

# 1. django 的项目的guest子目录下通过urls.py文件来定义URLconf
#　2. 但是,在urls.py文件中只找到一个admin/路径的路由配置
#　3. 当前url和index/并没有匹配

# 导入sign应用到views文件


# 定义index函数,并通过HttpResponse类想客户端(浏览器)返回字符串"hello django"
# HttpResponse类在django.http.HttpResponse中,以字符串的形式传递给客户端



#　２．２．４　　使用模板

# 在应用sign/目录下创建templates/index.html 文件．

# 修改视图文件views.py中的index函数

# 使用模板是，抛弃HttpResponse类，转而使用Django的render函数．request为请求对象,'index.html'为返回给客户端的HTML页面

# 2.3 django的工作流

#　2.3.1　　URLconf

# 为了给一个应用设计url需要创建Python模块,这个python模块通常成为URLconf.这个模块包含URL模式(简单的正则表达式)到视图函数(默认views.py文件中的函数)的简单映射

# python中正的匹配符

# r  字符串前面加"r"为放置被转义
# ^ 　匹配字符串开头：在多行行模式中匹配每一行的开头
# $ 　匹配字符串开头：在多行行模式中匹配每一行的末尾

#  django处理一个请求的过程如下
#  1.django使用的是根URLconf模块.这个值通常是通过ROOT_URLCONF设置
# 2. django加载URLconf模块(urls.py文件), 并讯号可用的urlpatterns
# 3. django依次匹配每个url模式,在与请求的url匹配的第一个模式处停下来
# 4.一旦其中的一个正则表达式匹配上了,则django将请求指向对应的视图函数处理
# 5. 如果没有匹配到正则表达式,或过程中抛出了一个异常,则django将调用一个适当的错误处理视图


# 2.3.3 views 视图
# 视图函数,简称视图,是一个简单的Python函数,它就收web请求并且返回web响应.
# 响应可以是一张HTML网页,一个重定向,一个404错误,一个XML文档,或一张图片


# 2.3.4  temmpaltes模板

# 作为web框架,django需要一种非常便利的方法动态地生成HTML.常见的做法就是使用模板.


# 2.4 MTV开发模式

#　把数据存取逻辑，业务逻辑和表现逻辑组合在一起称为软件架构的ＭVC模式．


# １．　为什么要缩写


# ２．　MTV业务开发

# M:模型（数据存取层）　　　Ｔ:模板（表现层）　　　Ｖ:视图(业务逻辑)

