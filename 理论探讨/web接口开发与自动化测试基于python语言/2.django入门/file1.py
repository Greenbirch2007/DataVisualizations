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

#　2.3.1　　URL