# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TianqiItem(scrapy.Item):
    # define the fields for your item here like:
    # 地区
    area = scrapy.Field()
    # 采集来源url
    from_url = scrapy.Field()
    # 爬取时间
    bulid_time = scrapy.Field()
    # 日期
    day = scrapy.Field()
    # 最高温度
    max_temperature = scrapy.Field()
    # 最低温度
    min_temperature = scrapy.Field()
    # 天气
    weather = scrapy.Field()
    # 风向
    wind_direction = scrapy.Field()
    # 风力等级
    wind_power = scrapy.Field()
