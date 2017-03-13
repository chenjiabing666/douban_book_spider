# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author=Field()
    #page=Field()
    #price=Field()
    pingjia=Field()
    content=Field()
    author_jianjie=Field()
    #time=Field()
    name=Field()




