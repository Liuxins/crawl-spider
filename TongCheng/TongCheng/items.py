# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TongchengItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    # 浏览量
    view_num = scrapy.Field()
    # 申请人数
    apply_num = scrapy.Field()
    # 薪资水平
    salary = scrapy.Field()
    # 所属公司
    # company = scrapy.Field()
    # 更新时间/需判断，如果是今天就转化一下
    update_time = scrapy.Field()
    # 福利待遇
    welfare = scrapy.Field()
    # 需要人数
    need_num = scrapy.Field()
    # 学历
    edu = scrapy.Field()
    # 经验
    experience = scrapy.Field()
    # 地址
    address = scrapy.Field()
    # 职位描述
    job_desc = scrapy.Field()
    # 公司介绍/可能有的有图片所以xpath不一样，需要进行判断
    company_desc = scrapy.Field()

