

from pymysql import cursors,connect



# 连接数据库

conn = connect(
    host='127.0.0.1',
    user='root',
    password='123456',
    db='guest',
    charset='utf8mb4',
    cursorclass= cursors.DictCursor
)

try:
    with conn.cursor() as cursor:

        # 创建嘉宾数据
        sql = 'insert into guest (realname,phone,email,sign,event_id,create_time) values ("tom",180000002,"tom@mail.com",0,1,now());'
        cursor.execute(sql)

    # 提交事务

    conn.commit()


    with conn.cursor() as cursor:
        # 查询添加的嘉宾

        sql = ' select realname,phone,email,sign from guest where phone = %s'
        cursor.execute(sql,('180000002',))
        result = cursor.fetchone()
        print(result)

finally:
    conn.close()


#　在settings.py文件中设置mysql
#    DATABASES = {
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

