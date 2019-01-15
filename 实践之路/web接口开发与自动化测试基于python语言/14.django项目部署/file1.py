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

# 14.1.3  uWSGI运行Django


# 接下来通过uWSGI运行Django项目，此处假定django的项目路径为 /home/lk/DataVisualizations/djanto_rest

#  uwsgi命令常用参数如下


# 1. --http: 协议类型和端口号
#  2. --processes:开启的进程数量
# ３．　--workers: 开启的进程数量，等同于processes
# 4.  --chdir：指定运行目录
# 5. --wsig-file  载入 wsgi-file (加载wsgi.py文件)
#　６．　--stats:　在指定的地址上开启状态服务
# 　７．　--threads : 开启的进程数量
#  8. --master：允许　主进程存在
# 　９．　--daemonize:　使进程在后台运行，并将日志输出到指定的日志文件或UDPf服务器
# 10. --pidfile: 指定PID文件的位置,记录主进程的PID号(PID,服务进程ID)
# 11. --vacuum:  当服务器退出时自动清理环境,删除Unix Socket文件和PID文件


#   uwsgi --http :8000  --chdir /home/lk/DataVisualizations/djanto_rest  --wsgi-file djanto_rest/wsgi.py  -master --processes 4 --stat3 127.0.0.1:9191



#  14.2 Nginx

# nginx是一款轻量级的web服务器/反向大力服务器即电子邮件(IMAP/POP3)代理服务器并在一个BSD-like协议下发行


# 部署django常用 nginx + uWSGI .这个方案中,通常的做法是将Nginx作为服务器最前端,用它来接收web的所有请求,统一管理请求.
# ngixn可用来处理所有静态请求,这是nginx的强项.然后,nginx将所有非静态请求通过uWSGI传递给Django,由Django来进行处理,从而
# 完成一次web请求.可见,uWSGI的租用类似于一个桥接器,起到了连接nginx与django的作用


#  14.2.1  安装nginx

#  sudo apt-get install install nginx

# nginx的基本操作

# 启动     /etc/init.d/nginx start
# 关闭     /etc/init.d/nginx stop
# 重启     /etc/init.d/nginx restart
# 查看版本  nginx  -v

# 修改nginx默认端口号,打开 /etc/nginx/sites-available/default 配置文件,修改端口号

#　将默认的80端口号修改为其他端口号，如8088．因为默认的80端口号通常会被其他程序占用．然后，通过上面的命令重启nginx
#　访问 http://127.0.0.1:8088/




#　14.2.2   Nginx+uWSGI+django

# 这里将三者整合起来，

# 在创建guest项目时，在guest/目录下默认已经生成了wsgi.py文件．创建django_uwsgi.ini文件，配置uWSGI参数，uWSGI支持多种类型的配置
#　文件，如果xml,ini等，次数使用ini类型

# django_uwsgi.ini
# 这个配置文件，相当于把"uwsgi"命令运行django项目的参数给文件化了

# socket:指定请求的方式和端口号．如果想直接通过uWSGI访问django项目，那么这里要配置为http；如果想通过nginx请求uWSGI来访问django项目
#  那么就要配置为socket

#  8888 为uWGI访问django项目的端口号
#  chdir:指定web项目的根目录
#  module:配置guest.wsgi.可以理解为这个配置,对于django_uwsgi.ini文件来说,与它平级的有一个guest/目录,这个目录下有一个wsgi.py文件

#  另外几个参数,可以参考前面uWSGI的常用参数说明

#  接下来切换到guest项目中,通过"uwsgi"命令读取django_uwsgi.ini文件启动web项目

# 注意查看uWSGI的启动信息,如果有错,就要检查配置文件的参数是否设置有误


#  接下来修改Nginx配置文件, 打开 /etc/nginx/sites-available/default文件,在文件底部添加如下配置

# 本机ip  123.138.108.45

# 一个简单的配置

#　listen 指定的是Nginx代理uWSGI对外的端口号
#　　server_name指定Nginx代理uWSGI对外的　IP地址；可以指定多个ip或域名，127.0.0.1访问的是本机
#  123.138.108.45是本机的ip地址，配置这个ip地址是为了给局域网内的其他主机访问

#　nginx是如何将请求转发给uWSGI的？主要是两行配置

#　include  /etc/nginx/uwsgi_params;
#　  uwsgi_pass 127.0.0.1:8000;

# include必须指定为uwsgi_params文件,如果启动失败,则需要指定该文件的绝对路径,通常在/etc/nginx/目录下;而uwsgi_pass所指的本机ip与
#　guest_uwsgi.ini配置文件中的ip端口号必须一致

#　配置完成后,保存退出default文件,重启nginx

# 访问页面时,请求会先到nginx,再有nginx转到uWSGI Web容器来处理(还是没有起来!)

# 修改的配置文件没有保存成功!


#  14.2.3  处理静态资源

#  当访问签到页面时,发现所有静态资源都无法访问了


#  打开/etc/nginx/site-available/default文件,添加web项目额静态资源


#  14.3  创建404页面

#  打开settings.py把DEBUG=False

# 把DEBUG设置为"False",关闭DEBUG后,需要设置  ALLOWED_HOST
# ALLOWED_HOST是了未来限定请求中的host值,以防止黑客构造包来发送请求,只有列表中的host才能访问.

#　一般不见以使用"*"通配符去配置