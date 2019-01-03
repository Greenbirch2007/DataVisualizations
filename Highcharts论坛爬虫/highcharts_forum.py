#! -*- coding:utf-8 -*-
import datetime
import time

from lxml import etree
import pymysql
from selenium import webdriver


driver = webdriver.Chrome()


def get_pages(url):
    driver.get(url)
    html = driver.page_source
    time.sleep(0.8)
    return html


def parse_page(html):
    big_list = []
    seletor = etree.HTML(html)
    title = seletor.xpath("//tr/th/a[2]/text()")
    link = seletor.xpath("//tr/th/a[2]/@href")
    for i1,i2 in zip(title,link):
        big_list.append((i1,'https://bbs.hcharts.cn/'+i2))

    return big_list


def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='list_learning',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:
        cursor.executemany('insert into highcharts_forum (title,link) values (%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass



if __name__ == '__main__':
    for offset in range(1,2):
        url = 'https://bbs.hcharts.cn/forum-77-' + str(offset) + '.html'
        html = get_pages(url)
        content = parse_page(html)
        insertDB(content)
        print(datetime.datetime.now())





#
# create table highcharts_forum(
#     id int not null primary key auto_increment,
# title varchar(88),
# link varchar(66)
# ) engine=Innodb default charset=utf8;
# #
# # #
# drop table scriptHome_python;