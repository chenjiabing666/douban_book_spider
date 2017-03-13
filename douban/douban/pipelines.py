# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import MySQLdb as db
class DoubanPipeline(object):
    def __init__(self):
        self.con=db.connect(user="root",passwd="chenjiabing",host="localhost",db="python",charset="utf8")
        self.cur=self.con.cursor()
        #self.cur.execute('use python')
        self.cur.execute("create table douban_book(id int auto_increment primary key,name varchar(100),author varchar(100),pingjia char(10),content varchar(5000),author_introduce varchar(5000))")
    def process_item(self, item, spider):
        self.cur.execute("insert into douban_book(id,name,author,pingjia,content,author_introduce) values(NULL,%s,%s,%s,%s,%s)",(item['name'],item['author'],item['pingjia'],item['content'],item['author_jianjie']))
        self.con.commit()
        return item

