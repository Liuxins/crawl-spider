# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LianjiaItem(scrapy.Item):
    # define the fields for your item here like:
    # define the fields for your item here like:
    # 小区名
    name = scrapy.Field()
    # 房间ｕｒｌ来源
    from_url = scrapy.Field()
    # 小区所在区域
    area = scrapy.Field()
    # 房屋总价
    total_prices = scrapy.Field()
    # 房屋单价
    unit_prices = scrapy.Field()
    # 房屋建筑面积
    floor_space = scrapy.Field()
    # 户型
    house_type = scrapy.Field()
    # 室内面积
    roon_area = scrapy.Field()
    # 建筑年份
    year = scrapy.Field()
    # 朝向
    orientation = scrapy.Field()
    # 装修情况
    fitment = scrapy.Field()
    # 供暖方式
    heating = scrapy.Field()
    # 产权年限
    age_limit = scrapy.Field()
    # 楼层
    house_floor = scrapy.Field()
    # 建筑类型
    bluid_type = scrapy.Field()
    # 电梯
    elevator = scrapy.Field()
    # 关注度
    attention = scrapy.Field()
    # 看房记录
    view = scrapy.Field()
    # 房屋简介
    introduce = scrapy.Field()
    # 中介人名
    intermediary = scrapy.Field()
    # 评分
    grade = scrapy.Field()
    # 挂牌时间
    hangtag = scrapy.Field()
    # 房间图片链接
    image_src = scrapy.Field()
    # 图片存储路径
    image_path = scrapy.Field()


