# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):     # 设置模板类
    # define the fields for your item here like:
    name = scrapy.Field()   #职位名称
    url = scrapy.Field()     # 链接
    category = scrapy.Field()   # 职位类别
    number = scrapy.Field()     # 数量
    address = scrapy.Field()    # 工作地点
    pub_time = scrapy.Field()   # 发布时间

    # 后续的详细内容也可以添加进去
    duty = scrapy.Field()   # 工作职责
    require = scrapy.Field()    # 招聘要求
    pass
