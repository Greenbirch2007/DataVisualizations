# 第５章django模板


# 系统登录功能开发完成,数据库表的设计已经完成

# 5.1  django-bootstrap3 拿护照呢



#  django-bootstrap3项目是将bootstrap3集成到django中，作为django的一个应用提供．好处是在django中用bootstrap会更烦吧

#  还要在settings.py中添加bootstrap3 应用


#  5.2 发布会管理

#  5.2.1  发布会列表

# 修改views.py


# 导入Model中的Event类,通过Event.objects.all() 查询所有发布会对象(数据),并通过render()方法附加在event_manage.html页面返回客户端


# 5.2.2  搜索功能


# 查询表单和登录表单一样,需要注意,method='get'为HTTP请求方式:action="/search_name/" 搜索请求路径:name="name"
#  搜索输入框的name属性值

# 在url.py文件中添加搜索路径的路由

# 在views.py中,创建search_name()视图函数

# 5.3 嘉宾管理
# 5.3.1  嘉宾列表

# 当前处理嘉宾管理页面,所以设置嘉宾菜单处于选中状态(class="activate").为发布菜单设置跳转路径(href="/event_manage/")

# urls.py中设置路由
# 在views.py中创建视图函数

#　导入Model中的Guest类，通过Guest.objects.all()查询所有嘉宾对象(数据)，并通过render()方法附加在guest_manage.html页面，并返回给客户端


# 5.3.2 分页器


#  django提供了Paginator类来实现分类功能．首先进入django的shell模式，练习Paginator类的基恩使用

# 导入Paginator类　　　from django.core.paginator import Paginator
# Guest下的所有表　　　　from sign.models import Guest
# 查询Guest表个所有数据   guest_list = Guest.objects.all()
#　创建每页２条数据的分页器　　　　p = Paginator(guest_list,2)
# 查询共多少　条数据　　　p.count
#　查询总共分几页　　p.page_range
# 获取第一页数据　　page1 = p.page(1)
# 当前第几页　　　page1
#　当前页的对　　page1.object_list
# 循环打印第１页嘉宾的realname


# 获取第二页数据　　　page2 = p.page(2)
# 本页第一条数据　　　　　page2.start_index()
# 本页最后一条数据　　　　page2.end_index()
# 是否有上一页　　　page2.has_previous()
# 是否有下一页　　page2.has_next()
# 上一页是第几页　　　page2.previous_page_number()
# 下一页是第几页　　　page2.next_page_number()


# 获取第３页数据　　　page3 = p.page(3)
# 是否有下一页　　　page3.has_next()
# 是否有上一页　　  page3.has_previous()
# 是否有其他页　　　　page3.has_other_pages()
# 前一页是第几页　　　page3.previous_page_number()

# 修改相应的视图函数，达到分页的不断


# 5.4 签到功能


# 对于发布会签到系统来说,最重要的是签到,而发布会管理功能额嘉宾管理功能都要服务于签到功能


#  5.4.1  添加签到链接


#　对于签到功能页面来说，它应该所属与某一场发布会．在打开签到页面之前，我们赢知道这是那一次那个的签到会
#　最好的方式是在发布列表中，给每一个发布会都提供一个"签到"链接，用来打开对应的签到页面


#　在event_manage.html页面,增加一列签到链接


# 当点击"sign"链接时,路径会默认跳转到"/sign_index/{{event.id}}"路径,
# 其中{{event.id}}为发布会的id.target="{{event.id}}_blank"属性设置链接在新窗口打开


#　修改urls.py文件中添加签到页面路径的路由

# (?P<eid>[0-9]+)匹配发布会id，而且必须为数字，匹配的数字eid将会作为sign_index()视图函数的参数

# 5.4.2  签到页面


#　views.py文件，创建sign_index()视图函数

# sign_index()函数获取从url配置得到的eid,作为发布会id的查询条件

# get_object_or_404,它默认调用django的table.objects.get()方法，如果查询的对象不存在，则会抛出一个Http404异常．
# 这就省去了对table.objects.get()方法的异常断言


# 5.4.3 签到功能并未开发完成，当用户在签到页面输入手机号，单击"签到"按钮后


# ５．５　退出系统

# 修改urls.py
