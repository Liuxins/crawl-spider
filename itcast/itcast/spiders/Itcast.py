# -*- coding: utf-8 -*-
import scrapy
# 导入链接提取器

"""这个是使用ｃｒａｗｌｓｐｉｄｅｒ类　使用原理为使用规则（Ｒｕｌｅ）来提取ｕｒｌ链接，并自动提交请求"""

#                                  这个为链接器
from scrapy.linkextractors import LinkExtractor
# 导入ｃｒａｗｌｓｐｉｄｅｒ类和Ｒｕｌｅ
from scrapy.spiders import CrawlSpider, Rule


class ItcastSpider(CrawlSpider):
    name = 'Itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://itcast.cn/']


    """ｒｕｌｅｓ是Ｒｕｌｅ对象的集合　用来匹配目标网站并排除干扰的，自动提取链接并提交请求的"""
    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = {}
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        return i


    '''
        针对ｃｒａｗｌｓｐｉｄｅｒ不能重写ｐａｒｓｅ方法　可以使用＿＿ｕｒｌ方法处理其实ｕｒｌ对应的相应
        ｐａｒｓｔ＿ｓａｔａｒ＿ｕｒｌ默认返回列表
    '''