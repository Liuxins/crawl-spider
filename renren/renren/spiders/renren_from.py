# -*- coding: utf-8 -*-
import scrapy

# post 请求为模拟登陆和填写数据　　使用的是FromRequest类　可以将表单中需要的信息写入并提交


class RenrenFromSpider(scrapy.Spider):
    name = 'renren_from'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def parse(self, response):
        data = {
            "email": "mr_mao_hacker@163.com",
            "password": "alarmchime",
        }

        # 特性为自动填写表单参数并将表单数据提交
        # 作用范围，天蝎表单数据
        #                                               formdata 表单参数　　
        yield scrapy.FormRequest.from_response(response,formdata=data,callback=self.parse_after)

    def parse_after(self,response):
        with open('renren_from.html','w')as f:
            f.write(response)

