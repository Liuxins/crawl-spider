# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SunItem(scrapy.Item):
    # define the fields for your item here like:
    # 编号
    id = scrapy.Field()
    # 详细页面的url
    detail_url = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 投诉内容
    content = scrapy.Field()

