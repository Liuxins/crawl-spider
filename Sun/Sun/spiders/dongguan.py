# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Sun.items import SunItem   # 导入模板类


class DongguanSpider(CrawlSpider):
    name = 'dongguan'
    # 允许的域名
    allowed_domains = ['wz.sun0769.com']
    # 起始的ｕｒｌ
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4']
    '''
     html/question/\d+/\d+.shtml
    index.php/question/questionType?type=\d+&page=\d+
    '''

    # 提取规则　
    rules = (
        #提取详情页面
        Rule(LinkExtractor(allow=r'html/question/\d+/\d+.shtml'), callback='parse_item', follow=False),
        # 提取翻页，会自动去重　只提取链接　不需要解析　所以不需要ｃａｌｌｂａｃｋ函数
        Rule(LinkExtractor(allow=r'questionType'),follow=True),
    )

    #解析数据
    def parse_item(self, response):
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        # print response.url,'--------------------========================='

        # 创建ｉｔｅｍ用于存放数据
        item = SunItem()

        # 解析数据
        item["id"] = response.xpath("/html/body/div[6]/div/div[1]/div[1]/strong/text()").extract_first().split(":")[-1]
        item["title"] = response.xpath("/html/head/title/text()").extract_first().split("_")[0]
        item["detail_url"] = response.url

        #　详情页面

        content = ''.join(response.xpath("/html/body/div[6]/div/div[2]/div[1]//text()").extract())
        if content.strip() == '':
            content = ''.join(response.xpath('//div[@class="contentext"]/text()').extract())
        item['content'] = content
        print item['id'],item['title'],item['detail_url'],item['content']

        #　将数据返回给引擎
        yield item