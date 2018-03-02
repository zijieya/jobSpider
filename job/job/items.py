# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item，Field

#定义job爬虫的数据结构
class JobItem(scrapy.Item):
    # define the fields for your item here like:
     profession = scrapy.Field()#职业
     description=scrapy.Field()#职位描述
     requirement=scrapy.Field()#要求
     companyName=scrapy.Field()#公司名称
     companyDescription=scrapy.Field()#公司简介
     scale=scrapy.Field()#规模
     companyCategory=scrapy.Field()#公司类别

    
