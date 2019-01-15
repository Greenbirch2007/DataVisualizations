

# 批量插入测试数据
#　这里给出了一种方法，制作文本文件的方式，然后让mysql的可视化工具来读取

f = open('guest.txt','w')
for i in range(1,3000):
    str_i = str(i)
    realname = 'jack' + str_i
    phone = 1399999 + i
    email = 'jack' + str_i + '@mail.com'
    sql = ' insert into sign_guest (realname,phone,email,sign,event_id ) values ("'+realname+'",'+str(phone)+',"'+email+'",0,1);'

    f.write(sql)
    f.write('\n')

f.close()