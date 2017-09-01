# -*- coding: utf-8 -*-
import scrapy,time
from TianQi.items import TianqiItem
from scrapy_redis.spiders import RedisSpider        # 1.导入热scrapy redis类



# 2. 修改继承类
# class TianqiSpider(scrapy.Spider):
class TianQiSpider(RedisSpider):

    name = 'tianqi'

   #  3.  注销允许的域名和起始的ｕｒｌ列表

    # allowed_domains = ['tianqi.com']
    # # 修改其实的ｕｒｌ
    # start_urls = ['http://lishi.tianqi.com/']

    # ---4.编写__init__ 动态获取允许的域名

    def __init__(self,*args,**kwargs):

        # 获取域名
        domain = kwargs.pop('domain','')
        # 赋值
        self.allowed_domains = filter(None,domain.split('.'))

        # 调用继承父类的初始化方法
        super(TianQiSpider, self).__init__(*args,**kwargs)


    # --5. 添加编写redis_key，用于从redis中获取其实的url
    redis_key = 'tianqi:start_urls'







        # 接收解析response

    def parse(self, response):
        # 首先是接收地区信息
        area_list = response.xpath("//div[@id='tool_site']/div[2]/ul/li/a/text()").extract()
        # 接收每个地区链接的信息来源
        area_url = response.xpath("//div[@id='tool_site']/div[2]/ul/li/a/@href").extract()

        # 遍历排除多余链接 并将他们一一对应
        for area, url in zip(area_list, area_url):

            if url == '#':
                continue  # 中断当前 继续
            yield scrapy.Request(url, callback=self.parse_area, meta={"area_1": area})

                # 根据每个的链接进入详情页 获取详情页具体信息

    def parse_area(self, response):
        # 继续地区参数
        area = response.meta["area_1"]

        # 刷选每一个月的url
        url_list = response.xpath("//div[@id='tool_site']/div[2]/ul/li/a/@href").extract()
        # 遍历每一个月的url列表 得到每一天的数据
        for url in url_list:
            # print url,'=============================================='
            # 创建请求 并发送 同时也将地域名床送过过去
            yield scrapy.Request(url, callback=self.parse_day, meta={'area_2': area})

    def parse_day(self, response):
        # 提取地区参数
        area = response.meta['area_2']
        # print response.url,area
        # 获取每一天的节点列表
        data_list = response.xpath('//div[@id="tool_site"]/div[@class="tqtongji2"]/ul')
        for data in data_list:
            print data
            # 实例化对象
            item = TianqiItem()

            # 地区
            item['area'] = area
            # url 来源
            item['from_url'] = response.url
            # 创建时间
            item['bulid_time'] = time.time()

            #
            # # 提取当月每天的日期
            item['day'] = data.xpath('./li[1]/text()').extract_first()
            if item['day'] == None:
                item['day'] = data.xpath('./li[1]/a/text()').extract_first()
            # 提取每天的的最高温度
            item['max_temperature'] = data.xpath('./li[2]/text()').extract_first()
            # 提取每天的的最低温度
            item['min_temperature'] = data.xpath('./li[3]/text()').extract_first()
            # 提取每天的的天气
            item['weather'] = data.xpath('./li[4]/text()').extract_first()
            # 提取每天的的风向
            item['wind_direction'] = data.xpath('./li[5]/text()').extract_first()
            # 提取每天的的风力等级
            item['wind_power'] = data.xpath("./li[6]/text()").extract_first()

            # print item.items()
            # for j,k in item.items():
            #     print j,k
            yield item
            #
            #
            #
