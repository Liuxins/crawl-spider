# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhiyoujiItem(scrapy.Item):
    # define the fields for your item here like:
    # 公司名称
    name = scrapy.Field()
    # 浏览次数
    views = scrapy.Field()
    # 评价人数
    evaluate = scrapy.Field()
    # 关注人数
    attention = scrapy.Field()
    # 企业类型
    category = scrapy.Field()
    # 人数
    human_count = scrapy.Field()
    # 行业
    industry = scrapy.Field()
    # 公司简称
    short_name = scrapy.Field()
    # 公司简介
    desc = scrapy.Field()
    # 好评度
    praise = scrapy.Field()
    # 薪酬范围
    salary_range = scrapy.Field()
    # 产品列表
    products = scrapy.Field()
    # 融资信息
    financing_info = scrapy.Field()
    # 关注度排名
    views_rank = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 网站
    website = scrapy.Field()
    # 联系方式
    phone = scrapy.Field()
    # qq
    qq = scrapy.Field()

