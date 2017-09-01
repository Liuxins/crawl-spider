# -*- coding: utf-8 -*-
from __future__ import print_function
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from LianJia.items import LianjiaItem

class LianjiaSpider(CrawlSpider):
    name = 'lianjia'
    allowed_domains = ['bj.lianjia.com']
    start_urls = ['https://bj.lianjia.com/ershoufang/pg1/']

    rules = (
        # 提取详情也ｕｒｌ并将ｒｅｓｐｏｎｓｅ返回给方法
        Rule(LinkExtractor(allow=r'\d+.html'), callback='parse_item', follow=False),
        # Rule(LinkExtractor(allow=r'https:\/\/bj\.lianjia\.com\/ershoufang\/\d+\.html'), callback='parse_item', follow=False),
        # 提取翻页等url
        Rule(LinkExtractor(allow=r'pg\d+'), follow=True)
    )

    def parse_item(self, response):
        # 为了避免埋雷　个人认为　走一步测试一步，埋雷一秒钟，找雷一整天

        '''测试是否已经链接上并能获取到信息'''
        # print response.url

        '''提取'''

        # 建立对象
        item = LianjiaItem()
        # 小区名
        item['name'] = response.xpath("//div[@class = 'communityName']/a[1]/text()").extract_first()
        # 链接来源
        item['from_url']= response.url
        # 小区所在区域
        area1 = response.xpath("//div[@class = 'areaName']/span[2]/a[1]/text()").extract_first()
        area2 = response.xpath("//div[@class = 'areaName']/span[2]/a[2]/text()").extract_first()
        area3 = response.xpath("//div[@class = 'areaName']/span[2]/text()[2]").extract_first()
        try:
            area4 = response.xpath("//div[@class = 'areaName']/a/text()").extract_first()
            area = area1 + ',' + area2 + ',' + area3 + ',' + area4
        except Exception as e:
            area = area1 + ',' + area2 + ',' + area3

        item['area'] = area

        # 房屋总价
        total1 = response.xpath("/html/body/div[5]/div[2]/div[2]/span[1]/text()").extract_first()
        total2 = response.xpath("/html/body/div[5]/div[2]/div[2]/span[2]/span/text()").extract_first()
        item['total_prices'] = total1+total2
        # 房屋单价
        unit_prices= response.xpath("/html/body/div[5]/div[2]/div[2]/div[1]/div[1]/span/text()").extract_first()
        item['unit_prices'] = str(unit_prices)+'元/平方米'

        # 户型
        item["house_type"] = response.xpath("//div[@id='introduction']/div/div/div[1]/div[2]/ul/li[1]/text()").extract_first()

        #房屋建筑面积
        item["floor_space"] = response.xpath("//*[@id='introduction']/div/div/div[1]/div[2]/ul/li[3]/text()").extract_first()
        # 室内面积
        item["roon_area"] = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[5]/text()').extract_first()
        # 建筑年份
        item['year'] = response.xpath('/html/body/div[5]/div[2]/div[3]/div[3]/div[2]/text()').extract_first()
        # 朝向
        item["orientation"] = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[7]/text()').extract_first()
        # 装修情况
        item['fitment'] = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[9]/text()').extract_first()
        # 供暖方式
        item['heating']= response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[11]/text()').extract_first()
        # 产权年限
        item['age_limit'] = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[13]/text()').extract_first()
        # 楼层
        item['house_floor'] = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[2]/text()').extract_first()
        # 建筑类型
        item['bluid_type'] = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[6]/text()').extract_first()
        # 电梯
        elevator1 = response.xpath('//*[@id="introduction"]/div/div/div[1]/div[2]/ul/li[12]/text()').extract_first()
        if elevator1 == u'有':
            elevator1 = '有电梯'
        else:
            elevator1 = '无电梯'
        item['elevator'] = elevator1
        # 关注度
        item['attention'] = response.xpath('//span[@id="favCount"]/text()').extract_first()+u'人关注'
        # 看房记录
        item['view'] = response.xpath('//span[@id="cartCount"]/text()').extract_first()+u'人看过'
        # 房屋简介
        item['introduce']=response.xpath("//div[@class='baseattribute clear']//div[@class='content']/text()").extract()
        # 中介人名
        item['intermediary']= response.xpath('/html/body/div[5]/div[2]/div[5]/div/div[1]/a[1]/text()').extract_first()
        # 评分
        item['grade']=response.xpath('/html/body/div[5]/div[2]/div[5]/div/div[1]/span/text()').extract_first().split('/')[0]
        # 挂牌时间
        item['hangtag']=response.xpath('//div[@id="introduction"]/div/div/div[2]/div[2]/ul/li[1]/text()').extract_first()
        #  房间图片链接
        item['image_src'] = response.xpath('//div[@id="thumbnail2"]/ul/li/@data-src').extract()

        # print (item)
        # print (item["intermediary"],item['grade'],item['hangtag'])


        yield item


