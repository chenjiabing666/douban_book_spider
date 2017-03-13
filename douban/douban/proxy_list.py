#coding:utf-8
import random
import scrapy
import logging
#ip代理的设置
class proxMiddleware(object):
    # def __init__(self):
    #     # self.file=open('reviewed_ips','r')
    #     self.proxy_list=[]
    #     # lines = self.file.readlines()
    #     for line in lines:
    #         self.proxy_list.append(line.strip('\n'))
    #     print self.proxy_list
    proxy_list=['http://222.187.227.40:10000', 'http://111.72.127.3:808', 'http://124.88.67.21:843', 'http://175.155.24.21:808', 'http://124.88.67.52:843', 'http://106.46.136.209:808', 'http://171.38.182.120:8123', 'http://106.46.136.153:808', 'http://182.88.104.101:8123', 'http://106.46.136.228:808', 'http://119.5.1.19:808', 'http://106.46.136.213:808', 'http://175.155.24.60:808', 'http://121.31.103.166:8123', 'http://180.76.154.5:8888', 'http://119.5.0.55:808', 'http://110.73.8.93:8123', 'http://110.73.13.136:8123', 'http://106.46.136.196:808', 'http://171.37.158.151:8123', 'http://110.73.10.248:8123', 'http://110.73.3.139:8123', 'http://110.73.7.122:8123', 'http://60.25.163.225:8118', 'http://110.73.167.221:8123']

    def process_request(self, request, spider):  #必须实现的方法
        # self.get_list_ips()
        request.meta['proxy']=random.choice(self.proxy_list)   #设置代理

