# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
# 导入ｕｓｅｒ－ａｇｅｎｔ列表清单
from LianJia.settings import USER_AGENT_LIST
# 导入代理ｉｐ池
from LianJia.settings import PROXIES
# 导入编码（加密）功能
import base64
# 导入随机
import random


class LianjiaSpiderMiddleware(object):
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


'''定义下载起中间件类'''

# 浏览器user-agent随机池
class RandomUserAgent(object):
    def process_request(self,spider,request):
        # 随即提取一个ｕｓｅｒ－ａｇｅｎｔ
        rondom_request_header = random.choice(USER_AGENT_LIST)
        # 修改用户头
        request.headers['User-Agent'] = rondom_request_header


# 代理ｉｐ池
class RandomProxy(object):
    def process_request(self,request,spider):
        # 随即选择代理池中的代理ｉｐ
        proxy = random.choice(PROXIES)
        # 判断代理ｉｐ中是否有帐号密码
        if proxy.has_key('user_passwd'):
            # 对帐号密码进行加密
            b64_user_pwd = base64.b64encode(proxy['user_passwd'])
            # 然后将编码之后的帐号和密码复制给请求对应的值
            request.headers['Proxy_Authorization'] = 'Basic '+ b64_user_pwd
            # 使用代理ｉｐ
            request.meta['proxy'] = 'http://'+proxy['ip_port']
