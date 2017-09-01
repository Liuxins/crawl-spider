# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AqiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    city = scrapy.Field()   # 城市
    day = scrapy.Field()   # 日期
    time_stamp = scrapy.Field() # 数据采集时间
    from_url = scrapy.Field()   #　数据来源

    # 数据

    aqi = scrapy.Field()    # aqi
    quality_grade = scrapy.Field()  # 空气质量等级
    pm2_5 = scrapy.Field()   # pm2.5
    pm10 = scrapy.Field()   #PM10
    so2 = scrapy.Field()    # SO2
    co = scrapy.Field()     #CO
    no2 = scrapy.Field()    # NO2
    o3_8h = scrapy.Field()  #O3
