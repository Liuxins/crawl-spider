# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):  #创建模板
    # define the fields for your item here like:
    movies_name = scrapy.Field()   # 电影名
    movies_score = scrapy.Field()   #评分
    movies_info = scrapy.Field()    #　电影信息
    movies_content = scrapy.Field() #　电影简介
