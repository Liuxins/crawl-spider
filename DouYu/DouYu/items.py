# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    # 房间名称
    room_name = scrapy.Field()
    # 房间id
    room_id = scrapy.Field()
    # 主播名称
    nick_name = scrapy.Field()
    # 主播id
    owner_uid = scrapy.Field()
    # 主播所在地
    anchor_city = scrapy.Field()
    # 图片链接
    image_src = scrapy.Field()
    # 图片储存路径
    image_path = scrapy.Field()

