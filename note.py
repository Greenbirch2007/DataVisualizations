


import os


themes = ['1.python学习必知','2.django入门','３．django视图','４．django模型','５．django模板','６．django测试','７．接口相关概念','８．开发web接口','９．接口测试工具介绍','１０．接口自动化测试框架','１１．接口的安全机制','１２．web services','13.REST','14.django项目部署','１５．接口性能测试']
base = '/home/lk/DataVisualizations/web接口开发与自动化测试基于python语言/'

for i in themes:
    file_name = base +  str(i)
    os.mkdir(file_name)