# 第4章 django模块下


# 在web应用中,以数据库驱动的网站在后台连接数据库服务器时,会从中取出一些数据然后在web页面用漂亮的格式展示这些数据.
#  这个网站也可能会向访问者提供修改数据库数据的方法.  复杂的网站会将数据搜索和数据增加两者集合起来



#  对于发布签到系统来说,也是以数据管理为主的网站,主要管理发布会和嘉宾数据.有一个观点,对于数据驱动的web系统,数据库表的设计完成,
#  就相当于web系统已经完成了一半,可见数据库表的设计难度以及在web开发中的重要性


#  4.1  设计系统表


#  django提供了完善的模型(model)层来创建和存取数据,它包含你所存储数据的必要的字段和行为.通常,每个模型对应数据库中唯一的一张表.所以,模型避免了
#  我们直接对数据进行操作


#  django模型的基础知识:

#  1. 每个模型是一个python类,继承django.db.models.Model类
#  2. 该模型的每个属性表示一个数据表字段
#  3. 所有这一切,已经给了你一个自动生成的数据库访问的api



#  嘉宾表中通过event字段(表中字段名为event_id)关联发布会id,一条嘉宾信息一定属于某一场发布会,ForeignKey()用来创建外键


# 嘉宾id作为主键吱哇,还可以通过发布会id+手机号z作为联合主键.Meta是django模型类的一个内部类,它用于定义一些django模型类的行为特性
# unique_together用于设置两个字段为联合主键



# python 将对象以str的方式展示处理

# python2    __unicode__()
# python3    __str__()

#　当模型创建好了以后，执行数据库迁移
# python manage.py makemigrations 应用名
#  python manage.py migrate



# 4.2  admin后台管理

# 通过admin后台管理用户/用户组非常方便,创建的发布会和嘉宾表同样可以通过admin后台管理

# django提供了大量选项让你针对特别的模块自定义管理工具.这些选项都在ModelAdmin类中,创建EventAdmin类ModelAdmin
#　z这里只自定义了一项：list_display,它是一个字段名称的数组，用于定义要在列表中显示哪些子弹．当然，这些字段名称必须是模型中的Event()类所定义的


#　修改admin.site.register()方法，添加EventAdmin类，可以理解为：用EventAdmin选项注册Event模块


# 除此之外，还可以迅速地生成搜索栏和过滤器，


# search_fields用于创建表字段的搜索器，可以设置搜索关键字匹配多个表字段
# list_filter用于创建字段过滤器


#　4.3 基本数据访问


#　python manage.py shell

# from sign.models import Event,Guest  导入sign应用下Model中的Event类和Guest类
# table.objects.all()    获得table  (即Event和Guest)中的所有对象


# 4.3.1   插入数据
# 尝试批量插入数据
# for item in range(3,3000):
    # time.sleep(0.6)
    # (e+{} % item) = Event(id={} %item, name='红米　Pro 发布会',limit=2000,status = True,address='北京水立方',start_time =datetime(2019,1,11,16,16,16) )fr


# 时间字段，在settings.py中设置，　UTC


# 可以使用table.objects.create()把　创建和保存两步一起完成



# 4.3.2   查询数据


# 查询数据是数据库表中使用频率最高的操作

#　table.objects.get()方法用于从数据库表中取得一条匹配的结果，返回一个对象，如果记录不存在的话，会报错

# table.objects.filter()方法是从数据库取得匹配的结果，返回一个对象列表，如果记录不存在的化，它会返回空列表[]

#Event.objects.filter(name__contains='发布会')


# name为发布会的字段名，在name和contains之间用双下划线连接．z这里contains部分会被django翻译成sql语句中的like语句

#　4.3.3  删除数据　　delete()



# 4.3.4  更新数据


# 4.4  sqlite管理工具

# 1.sqlite manager

# 4.5  配置　 mysql


# connect():建立数据库连接
# cursor():获取数据库操作游标
# execute()执行sql语句
# commit()提交数据执行
# close()关闭数据链接


#  4.5.4  在django中配置mysql

# 在settings.py中设置


# DATABASES = {
#     'default':{
#         'ENGINE':'django.db.backends.mysql',
#         'HOST':'127.0.0.1',
#         'PORT':'3306',
#         'NAME':'guest',
#         'USER':'root',
#         'POSSWORD':'123456',
#         'OPTIONS':{
#             'init_command':"SET sql_mode= 'STRICT_TRANS_TABLES'",
#
#         },
#     }
# }

# 配置信息从上到下一次是驱动(engine),主机地址(host),端口号(port),数据库(name),登录用户名(user),登录密码(password)


# 注意，切换了数据库后，之前在sqlite3数据库里的数据并不能复制到mysql数据库中，所以需要重新执行数据库同步，使数据模型重新在mysql中生成表

# python manage.py migrate
#  有一个坑，就是mysqldb
# 一个补救就是在应用的__init__.py 做一个准换

