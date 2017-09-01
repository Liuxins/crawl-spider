# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ZhiYouJi.items import ZhiyoujiItem
# 1.导入模板类
from scrapy_redis.spiders import RedisCrawlSpider
# 2. 修改继承类
class ZhiyoujiSpider(RedisCrawlSpider):
# class ZhiyoujiSpider(CrawlSpider):

    name = 'zhiyouji'
# 3. 修改允许的域名
    allowed_domains = ['jobui.com']
# 4. 修改起始的ｕｒｌ为动态获取

#     start_urls = ['http://www.jobui.com/cmp?area=全国&industry=互联网/电子商务']

# 5. 编写redis_key
    redis_key = 'crawlspider:start_urls'

    dx = 'area=%E5%85%A8%E5%9B%BD&industry=%E4%BA%92%E8%81%94%E7%BD%91%2F%E7%94%B5%E5%AD%90%E5%95%86%E5%8A%A1'
    rules = (
        # 先获取翻页等信息

        Rule(LinkExtractor(allow=r'/cmp\?'+dx+'\&n=\d+\#listInter/$'), follow=True),

        #  获取详情页面等信息
        Rule(LinkExtractor(allow=r'/company/\d+/$'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = ZhiyoujiItem()
        print response.url
        item['name'] = response.xpath('//*[@id="companyH1"]/a/text()').extract_first()
        # item['name'] = response.xpath('//*[@id="companyH1"]/a/text()').extract_first()
        item['views'] = response.xpath('//div[@class="grade cfix sbox"]/div[1]/text()').extract_first().split(u'过')[0].strip()
        # item["evaluate"] = response.xpath('//div[@class="grade cfix sbox"]/div[1]/text()').extract_first().split(u'评价')[0].split(u'浏览过')[1].strip()
        item["attention"] = response.xpath('//div[@class="grade cfix sbox"]/div[1]/text()').extract_first().split(u'评价')[1].strip()


        # 企业类型
        try:
            try:
                item['category'] = response.xpath('//*[@id="cmp-intro"]/div/div[2]/dl/dd[1]/text()').extract_first().split('/')[0]
            except:
                item['category'] = response.xpath('//*[@id="cmp-intro"]/div/div/dl/dd[1]/text()').extract_first().split('/')[0]
        except Exception as e:
            item['category'] = 'None'


        # 规模
        try:
            try:
                item['human_count'] = response.xpath('//*[@id="cmp-intro"]/div/div[2]/dl/dd[1]/text()').extract_first().split('/')[1]
            except:
                item['human_count'] = response.xpath('//*[@id="cmp-intro"]/div/div/dl/dd[1]/text()').extract_first().split('/')[1]
        except Ellipsis as e:
            item['human_count'] = "None"



        # 行业
        item['industry'] = response.xpath('//dd[@class="comInd"]/a[1]/text()').extract_first()
        # 简称
        item['short_name'] = response.xpath('//dl[@class="j-edit hasVist dlli mb10"]/dd[3]/text()').extract_first()
        # 简介
        item['desc'] = ''.join(response.xpath('//*[@id="textShowMore"]/text()').extract())


        # 好评度
        item['praise'] = response.xpath('//div[@class="swf-contA"]/div/h3/text()').extract_first()
        # 薪酬范围
        item['salary_range'] = response.xpath('//div[@class="swf-contB"]/div/h3/text()').extract_first()
        # 产品列表
        item['products'] = response.xpath('//div[@class="mb5"]/a/text()').extract()

        # 获取融资信息
        data_list = []
        node_list = response.xpath('//div[5]/ul/li')
        for node in node_list:
            temp = {}
            temp['date'] = node.xpath('./span[1]/text()').extract_first()
            temp['status'] = node.xpath('./h3/text()').extract_first()
            temp['sum'] = node.xpath('./span[2]/text()').extract_first()
            temp['investors'] = node.xpath('./span[3]/text()').extract_first()
            # 放到列表中
            data_list.append(temp)

        item['financing_info'] = data_list

        # 排名信息
        data_list = []
        node_list = response.xpath('//div[@class="fs18 honor-box"]/div')
        for node in node_list:
            temp = {}
            key = node.xpath('./a/text()').extract_first()
            # 将名次转换为整形
            temp[key] = int(node.xpath('./span[2]/text()').extract_first())
            data_list.append(temp)
            # for k,v in temp.items():
            #     print k,v
        item['views_rank'] = data_list

        # 地址信息
        item['address'] = response.xpath('//dl[@class="dlli fs16"]/dd[1]/text()').extract_first()
        # 网站
        item['website'] = response.xpath('//dl[@class="dlli fs16"]/dd[2]/a/text()').extract_first()

        # 联系方式
        item['phone'] = response.xpath('//div[@class="j-shower1 dn"]/dd/text()').extract_first()
        # qq
        item['qq'] = response.xpath('//dd[@class="cfix"]/span/text()').extract_first()


        yield item