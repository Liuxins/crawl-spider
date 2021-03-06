#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time    : 17-8-27 上午2:07
# @Author  : LiuXin
# @Site    : 
# @File    : redis2mongo.py
# @Software: PyCharm



import redis
from pymongo import MongoClient
import json


def convert():
    # 链接ｒｅｄｉｓ数据库
    redis_cli = redis.Redis(host="192.168.133.84",port=6379,db=0)

    # 先链接ｍｏｎｇｇｏｄｂ数据库
    mongo_cli = MongoClient('192.168.133.84',27017)
    db = mongo_cli['ZhiYouJi']    # 指定数据库
    col = db['zhiyouji']          # 指定集合名

    # 将数据从ｒｅｄｉｓ中d导出,然后在导入到ｍｏｎｇｇｏｄｂ中
    while True:

        #               先进先出　队列  从对应的键拿数据
        source,data = redis_cli.blpop(['zhiyouji:items'])


        # print(type(data),'data')
        item = json.loads(data)  # 转换ｊｓｏｎ数据
        # 插入ｍｏｎｇｇｏｄ

        # print(type(item))
        # print(item)
        col.insert(item)
        # print '++++++++++++'


if __name__ == "__main__":
    convert()