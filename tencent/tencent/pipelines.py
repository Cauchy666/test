# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymongo
class TencentPipeline(object):
    def __init__(self):
        # self.filename = open('tencent.json','w')
        client = pymongo.MongoClient(host='localhost',port=27017)
        self.db = client['tencent']
        self.coll = self.db['tencent']




    def process_item(self, item, spider):

        # text = json.dumps(dict(item),ensure_ascii=False)+",\n"
        # self.filename.write(text.encode('utf-8'))

        postItem = dict(item)
        self.coll.insert(postItem)
        return item

