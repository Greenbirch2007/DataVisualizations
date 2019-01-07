# 　第３章　django视图


# ３．１　来写个登录功能

# 当输入用户名密码并点击"登录"按钮之后，登录表单(form)中的数据要以什么方式(get/post)提交到服务器端？
# django如何验证用户名/密码的正确性?
# 如果验证成功应该如何处理？
# 如果验证失败又如何将错误返回客户端？



# ３．１．１　　get与post请求


# 当　客户端通过http协议想服务器提交请求时，最常用的是get和post

# get :从指定的资源请求数据
# post:向指定的资源提交要别处理的数据

# １．　ｇｅｔ请求
# 先来　看看get方法是如何传参数的,给form表单添加属性method="get"

# get方法会将用户提交的数据添加到url地址中，路径后面跟问好＂？＂
# username为HTML代码中<input>标签的name属性值(name="username"),admin是我们在用户名输入框中填写的用户名．
# password=admin123的取值方式与用户名相同．多个参数之间用"&"符号隔开

# ２．　post请求

# 将form表单中的属性修改为method="post"


#　跨站请求伪造(Cross-Site Request Forgery,CSRF)漏洞

# django针对CSRF的保护措施是在生成的每个表单中放置一个自动生成的令牌．通过这个令牌判断post请求是否来自　同一个网站
# 之前的模板都是纯粹的Ｈｔｍｌ,这里首次用到django的模板，使用"模板标签"(Tempalte Tag)添加CSRF令牌．
# 在表单中添加{% csrf_token %}


# 源代码中多了一个csrfmiddlewaretoken参数，当页面向django服务器发送一个post请求时，服务器端要求客户端加上csrfmiddlewaretoken字段，
# 该字段的值为当前会话id加上一个密钥的散列值
# 如果想忽略掉该检查，那就settings.py文件中注释掉csrf
# 'django.middleware.csrf.CsrfViewMiddleware',


# 3.1.2  处理登录请求

#  现在知道了将表单中的数据提交给服务器的两种方式(get/post)，那么django服务器是如何接收的数据并加以处理
#  可以通过form表单的action属性来指定提交的路径．  action="/login_action/">



# 当我们填写用户名/密码,单击"登录"按钮时，有http:127.0.0.1:8000/login_aciton/路径来提交登录请求．　下面修改urls.py的路由设置

# 登录请求由views.py视图文件的login_action函数来处理，打开views.py文件，编写login_action视图函数



