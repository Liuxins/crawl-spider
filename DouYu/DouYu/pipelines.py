# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os,scrapy

# 另一种方法，导入非同级目录文件.路径
from scrapy.utils.project import get_project_settings

# 导入图片储存管道
from scrapy.pipelines.images import ImagesPipeline

class DouyuPipeline(object):
    def process_item(self, item, spider):
        return item


# 创建管道 继承图片管道父类
class ImagePipeline(ImagesPipeline):
    # 图片储存路径等
    IMAGES_STORE = get_project_settings().get("IMAGES_STORE")

    # 将要下载的图片文件ｕｒｌ创建请求并提交给引擎
    def get_media_requests(self, item, info):
        # print item['image_src'],'==========='
        yield scrapy.Request(item["image_src"])

    # 更改图片名称
    def item_completed(self, results, item, info):
        image = [data['path'] for ok,data in results if ok]
        # print image

        # 拼接　路径名字
        old_name = self.IMAGES_STORE + os.sep +image[0]
        new_name = self.IMAGES_STORE + os.sep + image[0].split(os.sep)[0] +os.sep + item['nick_name'] + '.jpg'

        os.rename(old_name,new_name)
        item['image_path'] = new_name

        return item