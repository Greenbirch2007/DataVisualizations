# 第１４章　　django项目部署


#  14.uWSGI
#  14.1.1 uWSGI介绍

#  uWSGI是一个web服务器,它实现了WSGI,uswgi,HTTP等协议,在nginx中,ngx_http_uwsgi_module的作用是与uWSGI服务器进行交换


#　WSGI, uwsgi,uWSGI三者之前的关系

#  1. WSGI是web服务器与web应用程序或应用框架之间的接口,也可以看做一个协议.
#  2. uwsgi是一种传输协议
#  3. uWSGI是实现了uwsgi和WSGI两种协议的web服务器

#　uwsgi协议是一个uWSGI服务器自带的协议，它用于定义传输信息的类型，每一个uwsgi　packet的前4 byte都为传输信息类型描述，
# 它与WSGI相比是不同的两个协议


# １４．１．２　　安装　uWSGI

