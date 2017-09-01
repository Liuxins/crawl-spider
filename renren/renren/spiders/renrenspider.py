# -*- coding: utf-8 -*-
import scrapy

# post 请求为模拟登陆和填写数据　　使用的是FromRequest类　可以将表单中需要的信息写入并提交


class RenrenspiderSpider(scrapy.Spider):
    name = 'renrenspider'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/PLogin.do']

    def start_requests(self):
        # 用ｐｏｓｔ方法请求
        url = self.start_urls[0]
        data={
            "email": "mr_mao_hacker@163.com",
            "password": "alarmchime",
            }
        # 特性为自动填写表单参数并将表单数据提交
        # 作用范围，填写表单数据
        #                                               formdata 表单参数　
        yield scrapy.FormRequest(url,callback=self.parse,formdata=data)

    def parse(self, response):
        with open('./renren.html','w')as f:
            f.write(response.body)
