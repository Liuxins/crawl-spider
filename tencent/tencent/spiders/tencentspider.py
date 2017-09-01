# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem   # 为爬虫导入item模板

class TencentSpiderSpider(scrapy.Spider):
    name = "tencentspider"
    allowed_domains = ["tencent.com"]   #域名局限
    start_urls = (
        'http://hr.tencent.com/position.php/',
    )
    # 提取数据　保存数据
    def parse(self, response):
        # 获取所有职位的节点　　先获取那内容等
        node_list = response.xpath("//tr[@class='even']|//tr[@class='odd']")
        # print "+=+"*60
        # print "*+-="*20,node_list
        host = 'http://hr.tencent.com/'

        for node in node_list:
            item= TencentItem() # 创建对象
            # 抽取数据
            #                                           extract_first()等同于extract[0]如果为空值不会报错 局限性为这个节点只有一条数据　若有多条则不行
            item['name'] = node.xpath('./td[1]/a/text()').extract_first()
            item['url'] = host + node.xpath('./td[1]/a/@href').extract_first()
            # category 作用是直接作用相同兄弟节点列数
            item['category'] = node.xpath('./td[2]/text()').extract_first()
            item['number'] = node.xpath('./td[3]/text()').extract_first()
            item['address'] = node.xpath('./td[4]/text()').extract_first()
            item['pub_time'] = node.xpath('./td[5]/text()').extract_first()

            # print item,'22222222222222222222222222222222222222222222222222222222'

            # for k,v in item.items():
            #     print k,v



            # # # 将数据返回给引擎
            # yield item

            # 创建新的请求，并发送获取新的内容 当前页的内容       # meta 将前面数据放入一个新的字典
            yield scrapy.Request(item['url'],callback=self.parse_detail,meta={"title":item})


            #　获取下一页ｕｒｌ
        next_url = host+response.xpath("//a[@id='next']/@href").extract_first()
        # print "="*50,next_url


        # 创建新请求，并返回引擎
        #                              callback参数为回调　就是点击前面的ｕｒｌ跳转
        yield scrapy.Request(next_url,callback=self.parse)

    # 定义
    def parse_detail(self,response):        # 这个是一个新的请求　获取这些详细内容的函数
        # 然后获取传递过来的ｉｔｅｍ
        item = response.meta['title']

        # 现在可以添加进到一个文件夹中了
        # 提取详细要求进入ｉｔｅｍ中 空字符串是将多条数据添加到一起
        item['duty']=''.join(response.xpath('//tr[3]/td/ul/li/text()').extract())
        item['require'] = ''.join(response.xpath('//tr[4]/td/ul/li/text()').extract())
        print item,'================================================================='
        # 然后返回数据