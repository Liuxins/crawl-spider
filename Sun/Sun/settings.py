# -*- coding: utf-8 -*-

# Scrapy settings for Sun project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Sun'

SPIDER_MODULES = ['Sun.spiders']
NEWSPIDER_MODULE = 'Sun.spiders'

MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
DATABASE_NAME = 'sun'
COLLECTIONS = 'sun_info'



# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Sun (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
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
#    'Sun.middlewares.SunSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Sun.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'Sun.pipelines.SunPipeline': 300,
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