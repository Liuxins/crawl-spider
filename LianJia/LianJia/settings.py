# -*- coding: utf-8 -*-

# Scrapy settings for LianJia project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import random


# 爬虫名
BOT_NAME = 'LianJia'

# 爬虫模块
SPIDER_MODULES = ['LianJia.spiders']
NEWSPIDER_MODULE = 'LianJia.spiders'

# 启用scrapy_redis的重复过滤器,那么这个时候，原来的过滤器将会被停用 ,这个是去重的作用
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 替换调度器为scrapy_redis的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 是否能从从断点(断掉的地方)继续爬取
SCHEDULER_PERSIST = True
# # 优先级队列
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# # 普通队列
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# # 栈
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

# 一定要为图片添加路径 后续会自动为存储在一个名为ｆｕｌｌ的文件夹中
IMAGES_STORE = '/home/python/Desktop/分布式爬虫/LianJia/LianJia'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'LianJia (+http://www.yourdomain.com)'

# USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'

# Obey robots.txt rules

# 为需要的随即ｕｓｅｒａｇｅｎｔ创建列表(模拟请求头)
USER_AGENT_LIST = [
    'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0",
    "zilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)",
    "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; DigExt) ",
    "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; TUCOWS) ",
    "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; .NET CLR 1.1.4322) ",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0 ) ",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0) ",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; by TSG) ",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.0.3705) ",
    "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0; .NET CLR 1.1.4322) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; en) Opera 8.0 ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0;) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; T312461) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1 ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; en) Opera 8.00 ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; TencentTraveler ) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; zh-cn) Opera 8.0 ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; zh-cn) Opera 8.50 ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.1.4322) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.1.4322; FDM) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; Maxthon; .NET CLR 1.1.4322) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; MathPlayer 2.0; .NET CLR 1.1.4322) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.0.3705; .NET CLR 1.1.4322) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; {FF0C8E09-3C86-44CB-834A-B8CEEC80A1D7}; iOpus-I-M) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; i-Nav 3.0.1.0F; .NET CLR 1.0.3705; .NET CLR 1.1.4322) ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.7) Gecko/20040616 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.0; ja-JP; rv:1.5) Gecko/20031007 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.0; rv:1.7.3) Gecko/20040913 Firefox/0.10 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.0; rv:1.7.3) Gecko/20041001 Firefox/0.10.1 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.0; ja-JP; m18) Gecko/20010131 Netscape6/6.01 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.7) Gecko/20040803 Firefox/0.9.3 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-DE; rv:1.7.5) Gecko/20041108 Firefox/1.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.0; de-DE; rv:1.7.5) Gecko/20041122 Firefox/1.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-GB; rv:1.7.5) Gecko/20041107 Firefox/1.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-GB; rv:1.7.5) Gecko/20041110 Firefox/1.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.7.5) Gecko/20041107 Firefox/1.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.0; fr-FR; rv:1.7.5) Gecko/20041108 Firefox/1.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.0; it-IT; rv:1.7.5) Gecko/20041110 Firefox/1.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US; rv:1.8b) Gecko/20050118 Firefox/1.0+ ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.6 Safari/532.0 ",
    "Mozilla/4.0 (Windows; U; Windows NT 5.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.33 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.27 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.55 Safari/525.19 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.0; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13",
    "Mozilla/4.8 [en] (Windows NT 5.1; U) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1); ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; MyIE2) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; FDM; ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1 ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; MyIE2) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; BrowserBob) ",
    "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0 ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Alexa Toolbar) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; TencentTraveler) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; zh-cn) Opera 8.0 ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; zh-cn) Opera 8.01 ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; zh-cn) Opera 8.50 ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.0.3705) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 2.0.40607) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; DFO-MPO Internet Explorer 6.0) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Maxthon; .NET CLR 1.1.4322) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; AOL 9.0; Windows NT 5.1; iebar; .NET CLR 1.0.3705) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.0.3705; .NET CLR 1.1.4322) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 1.0.3705) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.0.3705; .NET CLR 1.1.4322) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 1.0.3705) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.40607) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; NOKTURNAL KICKS ASS) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Maxthon; .NET CLR 1.1.4322; .NET CLR 2.0.41115) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; ENGINE; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT)) ",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; winfx; .NET CLR 1.1.4322; .NET CLR 2.0.50727; Zune 2.0) ",
    "Mozilla/4.0 (compatible; MSIE 5.0; Windows 98; DigExt); Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1); ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; ESB{F40811EE-DF17-4BC9-8785-B362ABF34098}; .NET CLR 1.1.4322) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.40607; .NET CLR 1.0.3705) ",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser; Avant Browser; .NET CLR 1.0.3705; .NET CLR 1.1.4322; Media Center PC 4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FDM) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FTDv3 Browser; .NET CLR 1.0.3705; .NET CLR 1.1.4322) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FunWebProducts; .NET CLR 1.1.4322; .NET CLR 2.0.40607) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; FunWebProducts; AtHome033) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; HCI0449; .NET CLR 1.0.3705) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; i-NavFourF; .NET CLR 1.1.4322) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Maxthon; ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Maxthon; .NET CLR 1.1.4322) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; MyIE2; .NET CLR 1.1.4322) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; MyIE2; Maxthon; .NET CLR 1.1.4322) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Q312461; FunWebProducts; .NET CLR 1.1.4322) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; Woningstichting Den Helder; .NET CLR 1.0.3705) ",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.1) ",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 1.0.3705; .NET CLR 2.0.50727; .NET CLR 1.1.4322) ",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322) ",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; SV1) ",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1) ",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30) ",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727) ",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648) ",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; InfoPath.1 ",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; EasyBits Go v1.0; InfoPath.1; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729) ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E) ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; BOLT/2.800) AppleWebKit/534.6 (KHTML, like Gecko) Version/5.0 Safari/534.6.3 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.48 Safari/525.19 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.33 Safari/530.5 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.55 Safari/534.3 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.151 Safari/534.16 ",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30 ChromePlus/1.6.3.1 ",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2 ",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; Lunascape 5.0 alpha2) ",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Lunascape 5.0 alpha2) ",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506; Tablet PC 2.0; Lunascape 5.0 alpha2) ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP; rv:0.9.4.1) Gecko/20020508 Netscape6/6.2.3 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP; rv:1.4) Gecko/20030624 Netscape/7.1 (ax) ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.4) Gecko/20030624 Netscape/7.1 (ax) ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.2) Gecko/20040804 Netscape/7.2 (ax) ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.6) Gecko/20040113 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; rv:1.7.3) Gecko/20040913 Firefox/0.10 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; rv:1.7.3) Gecko/20041001 Firefox/0.10.1 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP; rv:1.6) Gecko/20040206 Firefox/0.8 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP; rv:1.7) Gecko/20040614 Firefox/0.9 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP; rv:1.7) Gecko/20040707 Firefox/0.9.2 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.5) Gecko/20041107 Firefox/0.9.2 StumbleUpon/1.994 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; ja-JP; rv:1.7) Gecko/20040803 Firefox/0.9.3 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.7.5) Gecko/20041107 Firefox/1.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.7.5) Gecko/20041108 Firefox/1.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE; rv:1.7.5) Gecko/20041122 Firefox/1.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.7.5) Gecko/20041110 Firefox/1.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.5) Gecko/20041107 Firefox/1.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.5) Gecko/20041107 Firefox/1.0 StumbleUpon/1.999 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; es-ES; rv:1.7.5) Gecko/20041210 Firefox/1.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; fr-FR; rv:1.7.5) Gecko/20041108 Firefox/1.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; nl-NL; rv:1.7.5) Gecko/20041202 Firefox/1.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; sv-SE; rv:1.7.5) Gecko/20041108 Firefox/1.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8b) Gecko/20050118 Firefox/1.0+ ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; BOLT/2.340) AppleWebKit/530+ (KHTML, like Gecko) Version/4.0 Safari/530.17 UNTRUSTED/1.0 3gpp-gba ",
    "Mozilla/5.0 (Windows NT 5.1; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1 ",
    "Mozilla/5.0 (Windows NT 5.1; rv:2.1) Gecko/20110318 Firefox/4.0b13pre Fennec/4.0 ",
    "Mozilla/5.0 (Windows NT 5.1; rv:2.0b6pre) Gecko/20100902 Firefox/4.0b6pre Fennec/2.0b1pre ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2a1pre) Gecko/20090317 Fennec/1.0b1 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.2a1pre) Gecko/20081222 Fennec/1.0a2 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1 ",
    "Mozilla/5.0 (Windows; Windows; U; Windows NT 5.1; Windows CE 5.2; rv:1.8.1.4pre) Gecko/20070327 Minimo/0.020 ",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.16 Safari/537.36 ",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36 ",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.6 Safari/537.11 ",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3 ",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11 ",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6 ",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.872.0 Safari/535.2 ",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.864.0 Safari/535.2 ",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.860.0 Safari/535.2 ",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.815.0 Safari/535.1 ",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.813.0 Safari/535.1 ",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.810.0 Safari/535.1 ",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.809.0 Safari/535.1 ",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.792.0 Safari/535.1 ",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 ",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.724.100 Safari/534.30 ",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.25 (KHTML, like Gecko) Chrome/12.0.706.0 Safari/534.25 ",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.25 (KHTML, like Gecko) Chrome/12.0.704.0 Safari/534.25 ",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.700.3 Safari/534.24 ",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.43 Safari/534.24 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.21 (KHTML, like Gecko) Chrome/11.0.682.0 Safari/534.21 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.21 (KHTML, like Gecko) Chrome/11.0.678.0 Safari/534.21 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.19 (KHTML, like Gecko) Chrome/11.0.661.0 Safari/534.19 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.18 (KHTML, like Gecko) Chrome/11.0.661.0 Safari/534.18 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.134 Safari/534.16 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.634.0 Safari/534.16 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.602.0 Safari/534.14 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.600.0 Safari/534.14 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.599.0 Safari/534.13 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-CA) AppleWebKit/534.13 (KHTML like Gecko) Chrome/9.0.597.98 Safari/534.13 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.15 Safari/534.13 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.0 Safari/534.13 ",
    "Mozilla/5.0 (Windows U Windows NT 5.1 en-US) AppleWebKit/534.12 (KHTML, like Gecko) Chrome/9.0.583.0 Safari/534.12 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.548.0 Safari/534.10 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.9 (KHTML, like Gecko) Chrome/7.0.531.0 Safari/534.9 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.6 (KHTML, like Gecko) Chrome/7.0.500.0 Safari/534.6 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/7.0.0 Safari/700.13 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.53 Safari/534.3 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.461.0 Safari/534.3 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.458.1 Safari/534.3 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.8 (KHTML, like Gecko) Chrome/6.0.397.0 Safari/533.8 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.357.0 Safari/533.3 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.356.0 Safari/533.3 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.355.0 Safari/533.3 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.353.0 Safari/533.3 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.2 Safari/533.2 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.16 (KHTML, like Gecko) Chrome/5.0.335.0 Safari/533.16 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.288.1 Safari/532.8 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.4 Safari/532.2 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.3 Safari/532.2 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; de-DE) Chrome/4.0.223.3 Safari/532.2 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.2 Safari/532.2 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.1 Safari/532.2 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.7 Safari/532.2 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.5 Safari/532.2 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.4 Safari/532.2 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.3 Safari/532.2 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.12 Safari/532.2 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.0 Safari/532.2 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.221.6 Safari/532.2 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.5 Safari/532.1 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.4 Safari/532.1 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.3 Safari/532.1 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.0 Safari/532.1 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.213.1 Safari/532.1 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.213.0 Safari/532.1 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.212.0 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.7 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.4 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.2 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.0 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.209.0 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.208.0 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.206.1 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.206.0 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.204.0 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.2 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/525.13. ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.201.1 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.0 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.201.0 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198.0 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197.11 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.196.2 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.6 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML,like Gecko) Chrome/3.0.195.27 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.27 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.24 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.21 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.20 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.17 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.10 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.1 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.2 (KHTML, like Gecko) Chrome/3.0.191.3 Safari/531.2 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.0 (KHTML, like Gecko) Chrome/3.0.191.0 Safari/531.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.8 (KHTML, like Gecko) Chrome/2.0.178.0 Safari/530.8 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.8 (KHTML, like Gecko) Chrome/2.0.177.1 Safari/530.8 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.8 (KHTML, like Gecko) Chrome/2.0.177.0 Safari/530.8 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.7 (KHTML, like Gecko) Chrome/2.0.177.0 Safari/530.7 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.7 (KHTML, like Gecko) Chrome/2.0.176.0 Safari/530.7 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.7 (KHTML, like Gecko) Chrome/2.0.175.0 Safari/530.7 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.175.0 Safari/530.6 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.174.0 Safari/530.6 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.174.0 Safari/530.5 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.173.1 Safari/530.5 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.173.0 Safari/530.5 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.8 Safari/530.5 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.43 Safari/530.5 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.42 Safari/530.5 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.40 Safari/530.5 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.39 Safari/530.5 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.2 Safari/530.5 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.0 Safari/530.5 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.1 (KHTML, like Gecko) Chrome/2.0.170.0 Safari/530.1 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/530.1 (KHTML, like Gecko) Chrome/2.0.169.0 Safari/530.1 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/528.10 (KHTML, like Gecko) Chrome/2.0.157.2 Safari/528.10 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/528.9 (KHTML, like Gecko) Chrome/2.0.157.0 Safari/528.9 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/528.11 (KHTML, like Gecko) Chrome/2.0.157.0 Safari/528.11 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/528.10 (KHTML, like Gecko) Chrome/2.0.157.0 Safari/528.10 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/528.8 (KHTML, like Gecko) Chrome/2.0.156.1 Safari/528.8 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/528.8 (KHTML, like Gecko) Chrome/2.0.156.0 Version/3.2.1 Safari/528.8 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/528.8 (KHTML, like Gecko) Chrome/2.0.156.0 Safari/528.8 ",
    "Mozilla/4.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.59 Safari/525.19 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.55 Safari/525.19 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.50 Safari/525.19 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.43 Safari/525.19 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.39 Safari/525.19 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.4.154.18 Safari/525.19 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/528.4 (KHTML, like Gecko) Chrome/0.3.155.0 Safari/528.4 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.3.155.0 Safari/525.19 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.2.153.1 Safari/525.19 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.2.153.0 Safari/525.19 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.2.152.0 Safari/525.19 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.2.151.0 Safari/525.19 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.29 Safari/525.13 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13(KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13 ",
    "Opera/7.51 (Windows NT 5.1; U) [en] ",
    "Opera/8.0 (Windows NT 5.1; U; en) ",
    "Opera/8.0 (Windows NT 5.1; U; zh-cn) ",
    "Opera/9.80 (Windows NT 5.1; U; ru) Presto/2.7.39 Version/11.00 ",
    "Opera/9.80 (Windows NT 5.1; U; zh-tw) Presto/2.8.131 Version/11.10 ",
    "Opera/9.80 (Windows NT 5.1; U; Opera/9.80 (J2ME/MIDP; Opera Mini/5.0.18635/1030; U; en) Presto/2.4.15; ru) Presto/2.8.99 Version/11.10 ",
    "Opera/9.80 (J2ME/MIDP; Opera Mini/5.0(Windows; U; Windows NT 5.1; en-US)/23.390; U; en) Presto/2.5.25 Version/10.54 ",
    "Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.2.3) Gecko/23.377; U; en) Presto/2.5.25 Version/10.54 ",
    "Opera/9.80 (J2ME/MIDP; Opera Mini/(Windows; U; Windows NT 5.1; en-US) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54 ",
    "Opera/9.80 (Windows NT 5.1; Opera Mobi/49; U; en) Presto/2.4.18 Version/10.00 ",
    "HTC-ST7377/1.59.502.3 (67150) Opera/9.50 (Windows NT 5.1; U; en) UP.Link/6.3.1.17.0",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9 ",
    "Opera/9.80 (Windows NT 5.2; U; en) Presto/2.2.15 Version/10.10 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8 ",
    "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1 ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; .NET CLR 1.1.4322) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.41115) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; MyIE2; .NET CLR 1.1.4322) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; MyIE2; Maxthon; .NET CLR 1.1.4322) ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; rv:1.7.3) Gecko/20041001 Firefox/0.10.1 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.7.5) Gecko/20041107 Firefox/1.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.8b) Gecko/20050212 Firefox/1.0+ (MOOX M3) ",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; WOW64; Trident/4.0; uZardWeb/1.0; Server_USA) ",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; WOW64; Trident/4.0; uZardWeb/1.0; Server_KO_KTF) ",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; WOW64; Trident/4.0; uZard/1.0; Server_KO_SKT) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; WOW64; SV1; uZardWeb/1.0; Server_HK) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; WOW64; SV1; uZardWeb/1.0; Server_EN) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; WOW64; SV1; uZardWeb/1.0; Server_CN) ",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.2; SV1; uZardWeb/1.0; Server_JP) ",
    "Mozilla/5.0 (Windows NT 5.2; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.7 ",
    "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.813.0 Safari/535.1 ",
    "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.794.0 Safari/535.1 ",
    "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.792.0 Safari/535.1 ",
    "Mozilla/5.0 (Windows NT 5.2; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 ",
    "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.112 Safari/534.30 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.17 (KHTML, like Gecko) Chrome/11.0.652.0 Safari/534.17 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.558.0 Safari/534.10 ",
    "Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.15) Gecko/20101027 Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.540.0 Safari/534.10 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.540.0 Safari/534.10 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.4 (KHTML, like Gecko) Chrome/6.0.481.0 Safari/534.4 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.33 Safari/534.3 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.463.0 Safari/534.3 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.462.0 Safari/534.3 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.460.0 Safari/534.3 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.458.0 Safari/534.3 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/534.2 (KHTML, like Gecko) Chrome/6.0.454.0 Safari/534.2 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.99 Safari/533.4 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.126 Safari/533.4 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.2 Safari/532.2 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.6 Safari/532.2 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.221.6 Safari/532.2 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.5 Safari/532.1 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.3 Safari/532.1 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.213.1 Safari/532.1 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.213.0 Safari/532.1 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.212.0 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.210.0 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.206.1 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.2 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; de-DE) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.2 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.6 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.33 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.27 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.21 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/531.3 (KHTML, like Gecko) Chrome/3.0.193.2 Safari/531.3 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.43 Safari/530.5 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; eu) AppleWebKit/530.4 (KHTML, like Gecko) Chrome/2.0.172.0 Safari/530.4 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/530.4 (KHTML, like Gecko) Chrome/2.0.172.0 Safari/530.4 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.59 Safari/525.19 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.43 Safari/525.19 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.3.154.6 Safari/525.19 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.2.151.0 Safari/525.19 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.6 Safari/525.13 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.30 Safari/525.13 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.29 Safari/525.13 ",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7 ",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 ",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.8 (KHTML, like Gecko) Beamrise/17.2.0.9 Chrome/17.0.939.0 Safari/535.8 ",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 ",
    "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1 ",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0) ",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0) ",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0) ",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; Trident/6.0) ",
    "Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0 ",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.7.62 Version/11.01 ",
    "Opera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12 ",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0) ",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; Sleipnir/2.9.8) ",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0) ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.43 Safari/534.7 ",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.65 Safari/534.24 ",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.107 Safari/535.1 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.202 Safari/535.1 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7 ",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; MAGW; .NET4.0C; Lunascape 6.5.8.24780) ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1 Fennec/7.0a1 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.2a1pre) Gecko/20110331 Firefox/4.2a1pre Fennec/4.1a1pre ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b8) Gecko/20101221 Firefox/4.0b8 Fennec/4.0b3 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1 ",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.1) Gecko/20110318 Firefox/4.0b13pre Fennec/4.0 ",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.1) Gecko/20110318 Firefox/4.0b13pre Fennec/4.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2a1pre) Gecko/20090317 Fennec/1.0b1 ",
    "Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows; U; Windows NT 6.1; sv-SE) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54 ",
    "Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/24.838; U; id) Presto/2.5.25 Version/10.54 ",
    "Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54 ",
    "Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/22.478; U; en) Presto/2.5.25 Version/10.54 ",
    "Opera/9.80 (J2ME/MIDP; Opera Mini/5.0 (Windows NT 6.1; WOW64) AppleWebKit/23.411; U; en) Presto/2.5.25 Version/10.54 ",
    "Opera/9.80 (J2ME/MIDP; Opera Mini/4.3.24214 (Windows; U; Windows NT 6.1) AppleWebKit/24.838; U; id) Presto/2.5.25 Version/10.54 ",
    "Opera/9.80 (Windows NT 6.1; Opera Mobi/49; U; en) Presto/2.4.18 Version/10.00 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1623.0 Safari/537.36 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36 ",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1468.0 Safari/537.36 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36 ",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.60 Safari/537.17 ",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1284.0 Safari/537.13 ",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3 ",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11 ",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.8 (KHTML, like Gecko) Chrome/17.0.940.0 Safari/535.8 ",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.77 Safari/535.7ad-imcjapan-syosyaman-xkgi3lqg03!wgz ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.7xs5D9rRDFpg2g ",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.8 (KHTML, like Gecko) Chrome/16.0.912.63 Safari/535.8 ",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.861.0 Safari/535.2 ",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.815.10913 Safari/535.1 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.814.0 Safari/535.1 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.813.0 Safari/535.1 ",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.812.0 Safari/535.1 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.811.0 Safari/535.1 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.810.0 Safari/535.1 ",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.801.0 Safari/535.1 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/526.3 (KHTML, like Gecko) Chrome/14.0.564.21 Safari/526.3 ",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.215 Safari/535.1 ",
    "Mozilla/5.0 (Windows NT 6.1; en-US) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.750.0 Safari/534.30 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.53 Safari/534.30 ",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.113 Safari/534.30 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/12.0.702.0 Safari/534.24 ",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/12.0.702.0 Safari/534.24 ",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.699.0 Safari/534.24 ",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.697.0 Safari/534.24 ",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.68 Safari/534.24 ",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.3 Safari/534.24 ",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.12 Safari/534.24 ",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.694.0 Safari/534.24 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.669.0 Safari/534.20 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.17 (KHTML, like Gecko) Chrome/11.0.655.0 Safari/534.17 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.17 (KHTML, like Gecko) Chrome/11.0.654.0 Safari/534.17 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.17 (KHTML, like Gecko) Chrome/10.0.649.0 Safari/534.17 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE) AppleWebKit/534.17 (KHTML, like Gecko) Chrome/10.0.649.0 Safari/534.17 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.134 Safari/534.16 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru-RU; AppleWebKit/534.16; KHTML; like Gecko; Chrome/10.0.648.11;Safari/534.16) ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; ru-RU) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.11 Safari/534.16 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.11 Safari/534.16 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.638.0 Safari/534.16 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.19 Safari/534.13 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.0 Safari/534.13 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.596.0 Safari/534.13 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.224 Safari/534.10 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.540.0 Safari/534.10 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.540.0 Safari/534.10 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.6 (KHTML, like Gecko) Chrome/7.0.498.0 Safari/534.6 ",
    "Mozilla/5.0 (ipad Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.6 (KHTML, like Gecko) Chrome/7.0.498.0 Safari/534.6 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.464.0 Safari/534.3 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.461.0 Safari/534.3 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.460.0 Safari/534.3 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.459.0 Safari/534.3 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.458.1 Safari/534.3 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.2 (KHTML, like Gecko) Chrome/6.0.454.0 Safari/534.2 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.428.0 Safari/534.1 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.428.0 Safari/534.1 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.9 (KHTML, like Gecko) Chrome/6.0.400.0 Safari/533.9 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/6.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.999 Safari/533.4 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.370.0 Safari/533.4 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.354.0 Safari/533.3 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.3 Safari/533.2 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.307.1 Safari/532.9 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.1.249.1025 Safari/532.5 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; it-IT) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.25 Safari/532.5 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.246.0 Safari/532.5 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.3 (KHTML, like Gecko) Chrome/4.0.227.0 Safari/532.3 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.3 (KHTML, like Gecko) Chrome/4.0.223.5 Safari/532.3 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.1 Safari/532.2 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.3 Safari/532.2 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.12 Safari/532.2 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.213.1 Safari/532.1 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.212.0 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.4 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.0 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.208.0 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.206.1 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.206.0 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.204.0 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.2 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.0 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.201.1 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197.11 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197.0 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.196.2 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.6 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.4 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.3 Safari/532.0 ",
    "Mozilla/6.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.27 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.27 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.21 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.10 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.1 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/531.4 (KHTML, like Gecko) Chrome/3.0.194.0 Safari/531.4 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/531.3 (KHTML, like Gecko) Chrome/3.0.193.2 Safari/531.3 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/531.0 (KHTML, like Gecko) Chrome/3.0.191.0 Safari/531.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/531.0 (KHTML, like Gecko) Chrome/2.0.182.0 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/531.0 (KHTML, like Gecko) Chrome/2.0.182.0 Safari/531.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/530.0 (KHTML, like Gecko) Chrome/2.0.182.0 Safari/531.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.174.0 Safari/530.6 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.43 Safari/530.5 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/530.4 (KHTML, like Gecko) Chrome/2.0.172.0 Safari/530.4 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/528.8 (KHTML, like Gecko) Chrome/2.0.156.1 Safari/528.8 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/528.8 (KHTML, like Gecko) Chrome/1.0.156.0 Safari/528.8 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.43 Safari/525.19 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.3.154.9 Safari/525.19",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14 ",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729) ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527 (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: ) ",
    "Mozilla/5.0 (Windows NT 6.0; rv:14.0) Gecko/20100101 Firefox/14.0.1 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1 ",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0) ",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0) ",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0) ",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/5.0) ",
    "Opera/9.25 (Windows NT 6.0; U; en) ",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506) ",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506; InfoPath.1) ",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0) ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.38 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.224 Safari/534.10 ChromePlus/1.5.2.0 ",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30618; Lunascape 4.7.3) ",
    "Mozilla/5.0 (Windows NT 6.0; rv:2.1.1) Gecko/20110415 Firefox/4.0.2pre Fennec/4.0.1 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.2a1pre) Gecko/20081222 Fennec/1.0a2 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1 ",
    "Opera/9.80 (Windows NT 6.0; Opera Mobi/49; U; en) Presto/2.4.18 Version/10.00 ",
    "Mozilla/5.0 (Windows NT 6.0) yi; AppleWebKit/345667.12221 (KHTML, like Gecko) Chrome/23.0.1271.26 Safari/453667.1221 ",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5 ",
    "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.45 Safari/535.19 ",
    "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11 ",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11 ",
    "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11 ",
    "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7 ",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.75 Safari/535.7 ",
    "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7 ",
    "Chrome/15.0.860.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/15.0.860.0 ",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.792.0 Safari/535.1 ",
    "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 ",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 ",
    "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.220 Safari/535.1 ",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.220 Safari/535.1 ",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.107 Safari/535.1 ",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.1 Safari/535.1 ",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.100 Safari/534.30 ",
    "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.699.0 Safari/534.24 ",
    "Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.34 Safari/534.24 ",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/534.24 (KHTML, like Gecko) Chrome/11.0.696.3 Safari/534.24 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.0 Safari/534.13 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/8.0.552.224 Safari/533.3 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.8 (KHTML, like Gecko) Chrome/7.0.521.0 Safari/534.8 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.458.1 Safari/534.3 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.127 Safari/533.4 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.5 Safari/533.2 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.1 Safari/533.2 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.241.0 Safari/532.4 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.3 (KHTML, like Gecko) Chrome/4.0.224.2 Safari/532.3 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.0 Safari/532.2 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.12 Safari/532.2 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.221.6 Safari/532.2 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.220.1 Safari/532.1 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.213.1 Safari/532.1 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.7 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.4 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.2 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.208.0 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.206.1 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.2 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0 (x86_64); de-DE) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.2 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.201.1 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.198.0 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197.11 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.196.2 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.6 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.3 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.27 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.21 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.20 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.17 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.10 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.1 Safari/532.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/531.3 (KHTML, like Gecko) Chrome/3.0.193.2 Safari/531.3 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/531.3 (KHTML, like Gecko) Chrome/3.0.193.0 Safari/531.3 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.7 (KHTML, like Gecko) Chrome/2.0.176.0 Safari/530.7 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.174.0 Safari/530.6 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.173.1 Safari/530.5 ",
    "Mozilla/6.0 (Windows; U; Windows NT 6.0; en-US) Gecko/2009032609 Chrome/2.0.172.6 Safari/530.7 ",
    "Mozilla/6.0 (Windows; U; Windows NT 6.0; en-US) Gecko/2009032609 (KHTML, like Gecko) Chrome/2.0.172.6 Safari/530.7 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.6 Safari/530.5 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.43 Safari/530.5 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.40 Safari/530.5 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.39 Safari/530.5 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.23 Safari/530.5 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.2 Safari/530.5 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.4 (KHTML, like Gecko) Chrome/2.0.171.0 Safari/530.4 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.1 (KHTML, like Gecko) Chrome/2.0.168.0 Safari/530.1 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.1 (KHTML, like Gecko) Chrome/2.0.164.0 Safari/530.1 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.0 (KHTML, like Gecko) Chrome/2.0.162.0 Safari/530.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/530.0 (KHTML, like Gecko) Chrome/2.0.160.0 Safari/530.0 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/528.10 (KHTML, like Gecko) Chrome/2.0.157.2 Safari/528.10 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/528.11 (KHTML, like Gecko) Chrome/2.0.157.0 Safari/528.11 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/528.8 (KHTML, like Gecko) Chrome/2.0.156.1 Safari/528.8 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.59 Safari/525.19 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.50 Safari/525.19 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.46 Safari/525.19 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.43 Safari/525.19 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.42 Safari/525.19 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.4.154.31 Safari/525.19 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.2.153.0 Safari/525.19 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.2.152.0 Safari/525.19 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.2.151.0 Safari/525.19 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.6 Safari/525.13 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.30 Safari/525.13 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.29 Safari/525.13 ",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; de) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13 ",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3 ",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6 ",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0) Gecko/16.0 Firefox/16.0 ",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; Trident/5.0) ",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.2; WOW64; Trident/5.0) ",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0) ",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0) ",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0) ",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; ARM; Trident/6.0) ",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1667.0 Safari/537.36 ",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36 ",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.2 Safari/537.36 ",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36 ",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1464.0 Safari/537.36 ",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36 ",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15 ",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.14 (KHTML, like Gecko) Chrome/24.0.1292.0 Safari/537.14 ",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13 ",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13 ",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.26 Safari/537.11 ",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.17 Safari/537.11 ",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1229.94 Safari/537.4 ",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1 ",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3 ",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3 ",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24 ",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11 ",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.66 Safari/535.11 ",
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.65 Safari/535.11",
]


USER_AGENT = random.choice(USER_AGENT_LIST)
# 为代理ｉｐ建立随即列表 只买了一个代理ｉｐ　　对于爬虫来说　越多越好
PROXIES = [
  {"ip_port": "121.41.8.23:16816", "user_passwd": "morganna_mode_g:ggc22qxp"},
  {"ip_port": "61.137.206.50:8998"},
  {"ip_port": "182.88.199.116:8118"},
  {"ip_port": "138.68.16.252:3128"},
  {"ip_port": "125.112.170.50:24964"},
  {"ip_port": "113.124.92.31:35847"},
  {"ip_port": "60.167.133.92:44477"},
  {"ip_port": "115.221.122.13:37944"},
  {"ip_port": "106.46.203.194:38872"},
  {"ip_port": "106.42.196.26:29274"},
  {"ip_port": "49.84.181.244:36525"},
  {"ip_port": "60.167.133.229:24531"},
  {"ip_port": "183.158.0.42:46582"},
  {"ip_port": "113.121.171.147:35925"},
  {"ip_port": "113.121.171.147:35925"},
  {"ip_port": "207.154.222.11:8080"},
  {"ip_port": "162.243.171.75:8080"},
  {"ip_port": "27.106.62.214:8080"},
  {"ip_port": "59.46.96.28:8080"},
  {"ip_port": "103.255.15.24:8080"},
  {"ip_port": "203.144.137.194:8080"},
  {"ip_port": "38.96.9.162:8080"},
  {"ip_port": "45.76.55.34:8080"},
  {"ip_port": "101.200.44.5:8080"},
  {"ip_port": "49.85.3.239:32736"},
  {"ip_port": "222.85.50.3:48816"},
  {"ip_port": "125.109.198.245:41940"},
  {"ip_port": "115.215.49.43:41940"},
  {"ip_port": "113.121.184.236:43846"},
  {"ip_port": "220.162.73.10:40199"},
  {"ip_port": "123.55.186.234:35126"},
  {"ip_port": "222.85.39.79:47137"},
  {"ip_port": "106.3.94.15:31139"},
  {"ip_port": "61.143.16.81:33608"},
  {"ip_port": "194.44.176.116:3128"},
]

# 设定不止爬取限定的网站内容
ROBOTSTXT_OBEY = False

LOG_LEVEL = 'DEBUG'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs

# 设定下载延时 随即生成延时时间 防反爬
DOWNLOAD_DELAY = random.uniform(1,4)

# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'LianJia.middlewares.LianjiaSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html

# 开启下载器中间件
DOWNLOADER_MIDDLEWARES = {
   'LianJia.middlewares.RandomUserAgent': 543,  # 将中间类注册
   'LianJia.middlewares.RandomProxy': 544,      # 将中间件注册

}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html

# 开启存储管道　为管道权重赋值
ITEM_PIPELINES = {
   'LianJia.pipelines.LianjiaPipeline': 300,
   'LianJia.pipelines.ImagePipeline': 500, # 改个名　为了方便确认
    # 开启ｒｅｄｉｓ的管道存储
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'



# 开启ｒｅｄｉｓ的链接地址
REDIS_URL = 'redis://192.168.0.104:6379'









# # -*- coding: utf-8 -*-
#
#
# #coding:utf-8
# # Scrapy settings for example project
# #
# # For simplicity, this file contains only the most important settings by
# # default. All the other settings are documented here:
# #
# #     http://doc.scrapy.org/topics/settings.html
# #
# SPIDER_MODULES = ['LianJia.spiders']
# NEWSPIDER_MODULE = 'LianJia.spiders'
#
# USER_AGENT = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13 '
#
# # 启用scrapy_redis的重复过滤器,那么这个时候，原来的过滤器将会被停用 ,这个是去重的作用
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# # 替换调度器为scrapy_redis的调度器
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# # 是否能从从断点(断掉的地方)继续爬取
# SCHEDULER_PERSIST = True
# # # 优先级队列
# # SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# # # 普通队列
# # SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# # # 栈
# # SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"
#
# ITEM_PIPELINES = {
#     # 'Tianqi.pipelines.ExamplePipeline': 300,
#     'scrapy_redis.pipelines.RedisPipeline': 400,
# }
#
# LOG_LEVEL = 'DEBUG'
#
# # Introduce an artifical delay to make use of parallelism. to speed up the
# # crawl.
# # 下载延时
# DOWNLOAD_DELAY = 4
#
# REDIS_URL = 'redis://192.168.133.92:6379'
# BOT_NAME = 'LianJia'



