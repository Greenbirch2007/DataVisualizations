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

# 通过login_action函数来处理登录请求
# 客户端发送的请求信息全部包含在request中.关于如何获取request中包含的信息,

# 首先,通过request.method得到客户端的请求方式,并判断其是否为POST方式的秦秋
# 接着,通过request.POST来获取POST请求.通过.get()方法获取'username'和'password'所获取的用户名/密码(admin/admin123).
# 如果参数为空,则返回一个空的字符串

# 注,此处的"username"和"password"对应form表单中<input>标签的name属性,可见这个属性的重要性


#  最后,通过if语句判断username和password的值是否为"admin/admin123".如果是则通过HttpResponse类返回字符串"login success!"
# 否则,将通过render返回index.html登录页面,并且顺带返回错误提示的字典"{'error':'username or password error!'}"

# 使用django的模板而言,添加{{error}},它对应render返回字典中的key,即'error',登录失败的页面中显示对应的value,即"username or password error!"
#  现在来体验下登录功能,分别看看登录成功和是吧的效果


#　３．１．３　登录成功页面


#  登录成功返回的"login success!"　字符串只是一种临时方案，只是为了方便验证登录的处理逻辑，现在验证没有问题之后，需要通过HTML页面来替换

#　我们要开发的是发布会签到系统，那么登录之后默认应该是什么？应该是显示发布会管理页面．


#　首先，创建　event_manage.html页面
# 此处又用到了一个新的类HttpResponseRedirect，它可以对路径进行重定向从而在登录成功之后的请求指向/event_manage/目录，
#　即 http://127.0.0.1:8000/event_manage/

#　创建event_manage.html.,用于返回发布会管理页面event_manage.html

#　最后在urls.py中添加路由

#  #3.2  Cookie和Session


# cookie机制:cookie分发通过扩展http协议来实现的,服务器通过在http的响应头中加上一行特殊的指示来提示浏览器按照指示生成响应的cookie
# 而cookie的使用则是由浏览器按照一定的原则在后台自动发送给服务器.浏览器检查所有存储的cookie,如果某个cookie所声明的作用范围大于等于
# 将要请求请求的资源所在的位置,则把该cookie附在请求资源的http请求头上发送给服务器

# session机制:session机制是一种服务器端的机制,服务器使用一种类似散列表的结构来保存信息

# 3.2.1  cookie的使用

# 修改views


