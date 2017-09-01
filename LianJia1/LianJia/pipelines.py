# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
reload(sys)
import json
sys.setdefaultencoding('utf8')      # 为了ｕｎｉｃｏｄｅ格式问题
# 导入库
import os,scrapy
# 导入存储路径　非统计目录
from scrapy.utils.project import get_project_settings
# 导入图片储存管道
from scrapy.pipelines.images import ImagesPipeline




class LianjiaPipeline(object):
    def __init__(self):
        # 创建存储的数据的文件
        # 打开文件
        self.file = open('./lianjiaershoufang.json','w+')


    def process_item(self, item, spider):   # 转化写入文件
        # 将ｉｔｅｍ转化成字典
        # data = dict(item)
        # 将字典转化为字符串
        data = json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.file.write(data)

        return item
    def close_spider(self,spider):
        self.file.close()
        print '保存成功'

# 创建一个管道　继承图片管道父类
class ImagePipeline(ImagesPipeline):
    # 图片存储路径等
    IMAGES_STORE = get_project_settings().get('IMAGES_STORE')

    # 将要下载的图片文件ｕｒｌ创建请求并提交给引擎
    def get_media_requests(self, item, info):
        for image_src in item['image_src']:
            # 获取图片
            yield scrapy.Request(image_src)
            # print image_src

    # 更改图片名称
    def item_completed(self, results, item, info):
        i = 0
        # print(results, "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        image = [data['path'] for ok,data in results if ok]
        print image, '============='
        count = len(item['image_src'])
        print(count, "-------------------------------------------------------")
        for i in range(count):
            # 拼接　路径名字
            old_name = self.IMAGES_STORE + os.sep +image[i]
            print old_name,"$$$$$$$$$$$$$$$$$$$$$$$$"
            new_name = self.IMAGES_STORE + os.sep + image[i].split(os.sep)[0] +os.sep + item['name'] + str(i) + '.jpg'
            print new_name,'&&&&&&&&&&&&'
            os.rename(old_name,new_name)
            i += 1
        item['image_path'] = new_name
    
        return item