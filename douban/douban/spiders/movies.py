# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from douban.items import DoubanItem

class MoviesSpider(CrawlSpider):
    name = 'movies'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250']


    #匹配规则 提取列表页面的ｕｒｌ　　通配ｕｒｌ规则  提取到的ｕｒｌ通过ｆｏｌｌｏｗ跳转
    rules = (           #　匹配所有翻页的节点
        Rule(LinkExtractor(allow=r'\?start=\d+\&filter='), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = DoubanItem()   #　实例化一个对象　直接继承ｉｔｅｍｓ模板
        # 获取所有电影清单上的节点
        movie_list = response.xpath('//div[@class="info"]')
        for movie in movie_list:
            # 电影名
            item['movies_name'] = movie.xpath('./div[1]/a/span[1]/text()').extract_first()
            # 电影评分
            item['movies_score']=movie.xpath('./div[2]/div/span[2]/text()').extract_first()
            # 获取电影信息
            item['movies_info']=movie.xpath('./div[2]/p[1]/text()').extract()
            # 获取电影简介
            item['movies_content']=movie.xpath('./div[2]/p[2]/span/text()').extract_first()
            print item
            # 返回ｉｔｅｍ
            yield item
        # i = {}
        # #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # #i['name'] = response.xpath('//div[@id="name"]').extract()
        # #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i
        #
