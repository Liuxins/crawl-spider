# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8') # 调用默认的给转化

class TencentPipeline(object):
    def __init__(self):
        # 创建存储数据的文件
        # 打开文件
        self.file = open('tentcent.json','w')


    def process_item(self,item,spider): # 转化写入文件
        # 将ｉｔｅｍ转换成字典
        # data = dict(item)
        #  将字典转化字符串
        data = json.dumps(dict(item),ensure_ascii=False)+'\n'

        self.file.write(data)
        return item

    def colse_spider(self,spider):
        self.file.close()
        print '保存成功８８８８８８８８８８８８８８８８８８８８８８８８８８８'