#　第13章 rest
#　rest同样属于web services技术范畴
# rest定义了一组体系架构原则,可以根据这些原则设计以系统资源为中心的web服务，包括使用不同语言编写的客户端如何通过HTTP处理和传输资源状态．

#  什么是restful架构

#  1. 每个url代表一种资源
#  ２．　客户端和服务器之间，传递这种资源的某种表现层
#  ３．　客户端通过四个HTTP动词，对服务器端资源进行操作，实现"表现层状态转化"


#  13.2 django rest framework

# django rest framework 是一套基于django的rest风格的框架
# 它具有的特点:
# 1. 功能强大,灵活,可以帮助你快速开发web api
# 2. 支持认证策略,包括OAuth 和OAuth2
# 3. 支持ORM和非ORM数据源的序列化
# 4. 丰富的文档以及良好的社区支持


# 13.2.1  创建简单的api


# 当django rest framework安装好之后,创建一个新的项目 django_rest,在项目下创建"api"应用


# 打开settings.py文件,添加应用 ,注意,要把rest_framework,api两个应用都一起添加


#  "rest_framework" 为django rest Framework应用，"api"为我们自己创建的应用，默认的权限策略可以设置在全局范围内，
#  通过DEFAULT_PERMISSION_CLASSES设置


#  通过migrate 命令执行数据库迁移
#  通过 createsuperuser命令创建超级管理员账户
#  创建数据序列化,在api应用下创建serializers.py文件



# Serializers用于定义api的表现形式,如返回哪些字段,返回怎样的格式等.这里序列化django自带的User和Group

# 编写视图文件,打开api应用下的views.py文件

# 在django rest framework中,viewsets用于定义视图的展现形式,例如返回哪些内容,需要哪些权限处理

#　在url中会定义相应的规则到ViewSet．ViewSet则通过serializer_class找到对应的Serializers.这里将User和Group的所有对象服务queryset,
# 并返回这些值，在UserSerializer和GroupSerializer中定义要返回的字段


#　在urls.py中，添加api的路由配置　（就是在项目下的urls.py文件中进行）

# 因为使用的是ViewSets，所以可以使用routers类自动生成URLconf

# 通过"runserver"来启动服务


# 13.2.2  添加接口数据

# 单击log in 登录超级管理员

# 13.2.3  测试接口

# 13.3  集成发布会系统api

# 根据发布会签到系统我们开发了相关的接口，而通过django rest framework来实现结构更加容易


#　１３．３．１　添加发布会api


# 接下来在django_rest项目的基础上增加发布会和嘉宾的相关接口
# 首先，创建模型,打开api应用下的models.py文件  跟之前web设计的数据模型一样

# 下面执行



