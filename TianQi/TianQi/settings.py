#coding:utf-8
# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
SPIDER_MODULES = ['TianQi.spiders']
NEWSPIDER_MODULE = 'TianQi.spiders'

USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'

# 启用scrapy_redis的重复过滤器,那么这个时候，原来的过滤器将会被停用
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

ITEM_PIPELINES = {
    # 'Tianqi.pipelines.ExamplePipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
# 下载延时
DOWNLOAD_DELAY = 1

REDIS_URL = 'redis://192.168.133.95:6379'






# 默认不写就是开启　Ｆａｌｓｅ为关闭
# LOG_ENABELD = False

# 编码格式默认为utf-8　
# LOG_ENCODING = 'UTF-8'

# 设置ｌｏｇ文件路径 默认呢的ｌｏｇ日志会消失，直接生成在文件中 设在当前项目文件中
# LOG_FILE = 'mylog.log'

# log等级
# 上线用INFO 　编码时勇敢ＤＥＢＵＧ
# LOG_LEVEL = 'INFO'

# CONCURRENT_REQUESTS
# 下载器并发数量设置，默认16
#
# DEPTH_LIMIT
# 爬取深度
#
# DOWNLOAD_TIMEOUT
# 下载超时
#
# CONCURRENT_ITEMS
# item管道同时处理item数量
#
# CONCURRENT_REQUESTS_PER_DOMAIN
# 域名的并发请求
#
# CONCURRENT_REQUESTS_PER_IP
# ip的并发请求数量

#===============================================











# # -*- coding: utf-8 -*-
#
# # Scrapy settings for Tianqi project
# #
# # For simplicity, this file contains only settings considered important or
# # commonly used. You can find more settings consulting the documentation:
# #
# #     http://doc.scrapy.org/en/latest/topics/settings.html
# #     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# #     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#
# BOT_NAME = 'Tianqi'
#
# SPIDER_MODULES = ['Tianqi.spiders']
# NEWSPIDER_MODULE = 'Tianqi.spiders'
#
#
# # Crawl responsibly by identifying yourself (and your website) on the user-agent
# #USER_AGENT = 'Tianqi (+http://www.yourdomain.com)'
#
# # Obey robots.txt rules
# ROBOTSTXT_OBEY = True
#
# # Configure maximum concurrent requests performed by Scrapy (default: 16)
# #CONCURRENT_REQUESTS = 32
#
# # Configure a delay for requests for the same website (default: 0)
# # See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# # See also autothrottle settings and docs
# #DOWNLOAD_DELAY = 3
# # The download delay setting will honor only one of:
# #CONCURRENT_REQUESTS_PER_DOMAIN = 16
# #CONCURRENT_REQUESTS_PER_IP = 16
#
# # Disable cookies (enabled by default)
# #COOKIES_ENABLED = False
#
# # Disable Telnet Console (enabled by default)
# #TELNETCONSOLE_ENABLED = False
#
# # Override the default request headers:
# #DEFAULT_REQUEST_HEADERS = {
# #   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
# #   'Accept-Language': 'en',
# #}
#
# # Enable or disable spider middlewares
# # See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# #SPIDER_MIDDLEWARES = {
# #    'Tianqi.middlewares.TianqiSpiderMiddleware': 543,
# #}
#
# # Enable or disable downloader middlewares
# # See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# #DOWNLOADER_MIDDLEWARES = {
# #    'Tianqi.middlewares.MyCustomDownloaderMiddleware': 543,
# #}
#
# # Enable or disable extensions
# # See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# #EXTENSIONS = {
# #    'scrapy.extensions.telnet.TelnetConsole': None,
# #}
#
# # Configure item pipelines
# # See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# #ITEM_PIPELINES = {
# #    'Tianqi.pipelines.TianqiPipeline': 300,
# #}
#
# # Enable and configure the AutoThrottle extension (disabled by default)
# # See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# #AUTOTHROTTLE_ENABLED = True
# # The initial download delay
# #AUTOTHROTTLE_START_DELAY = 5
# # The maximum download delay to be set in case of high latencies
# #AUTOTHROTTLE_MAX_DELAY = 60
# # The average number of requests Scrapy should be sending in parallel to
# # each remote server
# #AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# # Enable showing throttling stats for every response received:
# #AUTOTHROTTLE_DEBUG = False
#
# # Enable and configure HTTP caching (disabled by default)
# # See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# #HTTPCACHE_ENABLED = True
# #HTTPCACHE_EXPIRATION_SECS = 0
# #HTTPCACHE_DIR = 'httpcache'
# #HTTPCACHE_IGNORE_HTTP_CODES = []
# #HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

















































# # -*- coding: utf-8 -*-
#
# # Scrapy settings for TianQi project
# #
# # For simplicity, this file contains only settings considered important or
# # commonly used. You can find more settings consulting the documentation:
# #
# #     http://doc.scrapy.org/en/latest/topics/settings.html
# #     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# #     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#
# BOT_NAME = 'TianQi'
#
# SPIDER_MODULES = ['TianQi.spiders']
# NEWSPIDER_MODULE = 'TianQi.spiders'
#
# # USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36'
#
# # Crawl responsibly by identifying yourself (and your website) on the user-agent
# #USER_AGENT = 'TianQi (+http://www.yourdomain.com)'
#
# # Obey robots.txt rules
# ROBOTSTXT_OBEY = False
#
# # Configure maximum concurrent requests performed by Scrapy (default: 16)
# #CONCURRENT_REQUESTS = 32
#
# # Configure a delay for requests for the same website (default: 0)
# # See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# # See also autothrottle settings and docs
# #DOWNLOAD_DELAY = 3
# # The download delay setting will honor only one of:
# #CONCURRENT_REQUESTS_PER_DOMAIN = 16
# #CONCURRENT_REQUESTS_PER_IP = 16
#
# # Disable cookies (enabled by default)
# #COOKIES_ENABLED = False
#
# # Disable Telnet Console (enabled by default)
# #TELNETCONSOLE_ENABLED = False
#
# # Override the default request headers:
# #DEFAULT_REQUEST_HEADERS = {
# #   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
# #   'Accept-Language': 'en',
# #}
#
# # Enable or disable spider middlewares
# # See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# #SPIDER_MIDDLEWARES = {
# #    'TianQi.middlewares.TianqiSpiderMiddleware': 543,
# #}
#
# # Enable or disable downloader middlewares
# # See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# #DOWNLOADER_MIDDLEWARES = {
# #    'TianQi.middlewares.MyCustomDownloaderMiddleware': 543,
# #}
#
# # Enable or disable extensions
# # See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# #EXTENSIONS = {
# #    'scrapy.extensions.telnet.TelnetConsole': None,
# #}
#
# # Configure item pipelines
# # See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# #ITEM_PIPELINES = {
# #    'TianQi.pipelines.TianqiPipeline': 300,
# #}
#
# # Enable and configure the AutoThrottle extension (disabled by default)
# # See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# #AUTOTHROTTLE_ENABLED = True
# # The initial download delay
# #AUTOTHROTTLE_START_DELAY = 5
# # The maximum download delay to be set in case of high latencies
# #AUTOTHROTTLE_MAX_DELAY = 60
# # The average number of requests Scrapy should be sending in parallel to
# # each remote server
# #AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# # Enable showing throttling stats for every response received:
# #AUTOTHROTTLE_DEBUG = False
#
# # Enable and configure HTTP caching (disabled by default)
# # See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# #HTTPCACHE_ENABLED = True
# #HTTPCACHE_EXPIRATION_SECS = 0
# #HTTPCACHE_DIR = 'httpcache'
# #HTTPCACHE_IGNORE_HTTP_CODES = []
# #HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
