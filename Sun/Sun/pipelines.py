# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
from pymongo import MongoClient # 导入数据库

class SunPipeline(object):
    def __init__(self):
        ip = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']

        database_name = settings['DATABASE_NAME']
        collection = settings['COLLECTIONS']

        # 链接数据库
        self.handler = MongoClient(ip,port)
        # 选择数据库名
        self.db = self.handler[database_name]
        # 选择集合
        self.col = self.db[collection]

    def process_item(self,item,spider):
        data = dict(item)

        # 将数据插入数据库
        self.col.insert(data)
        return item



    def close_spider(self, item, spider):
        self.handler.close()
