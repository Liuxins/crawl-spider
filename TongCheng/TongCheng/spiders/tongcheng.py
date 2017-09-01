# -*- coding: utf-8 -*-
import scrapy
import time
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from TongCheng.items import TongchengItem
from scrapy_redis.spiders import RedisCrawlSpider


# 继承
class TongchengSpider(RedisCrawlSpider):
# class TongchengSpider(CrawlSpider):
    name = 'tongcheng'
    allowed_domains = ['bj.58.com']
    # start_urls = ['http://bj.58.com/tech/']
    redis_key = "tongcheng:start_urls"
    rules = (
        # 提取详情页url
        Rule(LinkExtractor(allow=r'tech/\d+x.shtml'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        # i = {}
        # i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
        # print(response.url, "************")
        # 实例化item对象
        # print(type(response), '***************')
        # print(response)
        item = TongchengItem()
        item['name'] = response.xpath('//div[@class="baseInfo_link"]/a/text()').extract_first()
        # print(item['name'], '********************')
        # 浏览量
        item['view_num'] = response.xpath('//*[@id="totalcount"]/text()').extract_first()
        # print(item['view_num'], '*************&********')
        # # 申请人数
        item['apply_num'] = response.xpath('//*[@id="apply_num"]/text()').extract_first()
        # # 薪资水平
        item['salary'] = response.xpath('//div[@class="pos_base_info"]/span[2]/text()').extract_first()
        # # 更新时间/需判断
        item['update_time'] = time.time()
        # # 福利待遇
        item['welfare'] = response.xpath('//div[@class="pos_welfare"]/span/text()').extract()
        # # 需要人数
        item['need_num'] = response.xpath('//div[@class="pos_base_condition"]/span[1]/text()').extract_first()[1]
        # # 学历
        item['edu'] = response.xpath('//div[@class="pos_base_condition"]/span[2]/text()').extract_first()
        # # 经验
        item['experience'] = response.xpath('//div[@class="pos_base_condition"]/span[1]/text()').extract_first()
        # # 地址
        item['address'] = response.xpath('//div[@class="pos-area"]/span[2]/text()').extract_first()
        # # 职位描述
        item['job_desc'] = response.xpath('//div[@class="posDes"]/div[1]/text()').extract()
        # # 公司介绍
        item['company_desc'] = response.xpath('//div[@class="intro"]/div/p/text()').extract_first()
        yield item
