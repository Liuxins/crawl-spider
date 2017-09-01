# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import base64     # 调用ｂａｓｅ４库进行加密,在此处成为编码模块

class TencentSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)



#  设置中间件
class Proxy(object):        # 中间件的用途在于反反爬虫　这个是下载中间件　还有个爬虫中间件
    # 建立一个ｐｒｏｃｅｓｓ＿ｒｅｑｕｅｓｔ方法　来处理请求
    #                        获得请求　　spider 固定参数
    def process_request(self,request,spider):
        # 功能　加用户头
        # 功能　加代理
        # 功能　使用ｓｅｌｅｎｉｕｍ获取动态加载数据

        # 先使用代理ｉｐ   需要花钱购买的　花钱的好  可以使用代理ｉｐ池子　加ｔｒｙ使用　被封就下一个继续
        proxy = {"ip_port": "121.41.8.23:16816", "user_passwd": "morganna_mode_g:ggc22qxp"}

        # proxy = {"ip_port": "144.255.48.162:20963"}

        # 对账号密码进行加密
        b64_user_pwd = base64.b64encode(proxy["user_passwd"])

        # 然后进行认证 为何要认证?　将请求的代理ｉｐ加入请求头
        # 固定用法
        request.headers["Proxy_Authorzation"] = 'Basic ' + b64_user_pwd
        #  # request.headers["Proxy_Authorzation"] = 'Basic '

        # 设置代理ip 就是使用
        # 固定用法                      # 网页地址
        request.meta["proxy"] = 'http://' + proxy['ip_port']
        # print request.meta,'1111111111111111111111111111111111111111111111111111111111'