# -*- coding: utf-8 -*-
import scrapy
import json
from DouYu.items import DouyuItem

class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    # 域名
    allowed_domains = ['capi.douyucdn.cn']
    # 保存 偏移量，接口
    offset = 0
    host = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=100&offset="
    # 起始的url请求
    start_urls = [host]

    def parse(self, response):
        # 将数据转换为字典
        res = json.loads(response.body)
        # 提取县官有用的内容
        data_list = res['data']

        # 遍历列表　取出单个　然后在利用
        for data in data_list:
            # 创建实例对象　储存单个信息
            item = DouyuItem()

            item['room_name'] = data["room_name"]   # 房间名称
            item['room_id'] = data["room_id"]       # 房间id
            item['nick_name'] = data["nickname"]    # 主播名称
            item['owner_uid'] = data["owner_uid"]   # 主播id
            item['anchor_city'] = data["anchor_city"]   # 主播所在地
            item['image_src'] = data["vertical_src"]    # 图片链接
            # item['image_path'] = data["room_name"]       # 图片储存路径

            # 返回数据给引擎
            yield item

            # 若得到数据不为空　可进行下一页的爬取
        if len(data_list) != 0:
            # 拼接下一次ｕｒｌ
            self.offset += 100
            next_url = self.host+str(self.offset)

            # 继续下一页的请求
            yield scrapy.Request(next_url,callback=self.parse)

