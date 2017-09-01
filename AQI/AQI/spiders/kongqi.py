# -*- coding: utf-8 -*-
import scrapy
import time
from AQI.items import AqiItem
# 1. 导入RedisSpider 类
from scrapy_redis.spiders import RedisSpider
# 修改继承类
class KongqiSpider(RedisSpider):
# class KongqiSpider(scrapy.Spider):

    name = 'kongqi'
# 3. 注销允许的域名和初始的url
#     allowed_domains = ['www.aqistudy.cn']
#     start_urls = ['https://www.aqistudy.cn/historydata/']


# 4. 　编写__init__()动态获取允许的域名
    def __init__(self,*args,**kwargs):  # 参数是为了承接后续给点ｕｒｌ动态取
        domain = kwargs.pop('domain','')
        print domain,'######################'
        self.allowed_domains = filter(None,domain.split(','))       # 切除ｄｏｍａｉｎｓ　若是没有获取到则切除空
        print self.allowed_domains,'$$$$$$$$$$$$$$$$$$$$$$$$'
        super(KongqiSpider, self).__init__(*args,**kwargs)

    # 5 .编写redis_key  这个是指纹码加密作用　防止重复
    redis_key = 'kongqi:start_urls'

    # 最初始的一定要去ｐａｒｓｅ
    def parse(self, response):
        url_list = response.xpath("//div[@class='bottom']/ul/div[2]/li/a/@href").extract()
        # 遍历列表然后跳转详情页面
        for url in url_list:
            city_url = "https://www.aqistudy.cn/historydata/"+url
            # print city_url,'=============='
            # 然后根据详细地址去匹配和获取页面
            yield scrapy.Request(city_url,callback=self.parse_month)

    def parse_month(self,response):
        # 得到上述月份ｕｒｌ中具体月份的ｕｒｌ.extract()
        month_url_list = response.xpath("//ul[@class='unstyled1']/li/a/@href").extract()

        for day_url in month_url_list:
            url = "https://www.aqistudy.cn/historydata/"+day_url
            # print url,'&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&'
    #         # 然后进入详情页面　进行提取
            yield scrapy.Request(url,callback=self.parse_day)

    def parse_day(self,response):
        # 获取所需要的内容
        node_list = response.xpath("//div[@class='panel-heading']/h3/text()")

        from_url = response.url
        city = response.xpath("/html/body/div[3]/div[1]/div[2]/div[1]/div[1]/h3").extract_first().split('2')[0]
        for node in node_list:
            item = AqiItem()
            item['city'] = city
            item['from_url'] = from_url
            item['time_stamp'] = time.time()
            item['day'] = node.xpath('./td[1]/text()').extract_first()
            item['aqi'] = node.xpath('./td[2]/text()').extract_first()
            item['quality_grade'] = node.xpath('./td[3]/span/text()').extract_first()
            item['pm2_5'] = node.xpath('./td[4]/text()').extract_first()
            item['pm10'] = node.xpath('./td[5]/text()').extract_first()
            item['so2'] = node.xpath('./td[6]/text()').extract_first()
            item['co'] = node.xpath('./td[7]/text()').extract_first()
            item['no2'] = node.xpath('./td[8]/text()').extract_first()
            item['o3_8h'] = node.xpath('./td[9]/text()').extract_first()
            print item
            yield item