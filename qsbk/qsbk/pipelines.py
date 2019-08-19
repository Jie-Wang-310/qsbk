# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html



'''数据量小可以使用'''
# import json

# class QsbkPipeline(object):
#
#     def __init__(self):
#         self.fp = open("duanzi.json", 'w', encoding='utf-8')
#
#     def open_spider(self, spider):   # 开始
#         print('爬虫开始了...')
#
#     def process_item(self, item, spider):  # 写入文件
#         item_json = json.dumps(dict(item), ensure_ascii=False)
#         self.fp.write(item_json+'\n')    #  \n是换行
#         return item
#
#     def close_spider(self, spider):  # 结束
#         self.fp.close()
#         print('爬虫结束了...')


'''一般不建议使用版本'''

# from scrapy.exporters import JsonItemExporter

# class QsbkPipeline(object):
#     def __init__(self):
#         self.fp = open("duanz.json", 'wb')
#         self.exporter = JsonItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
#         self.exporter.start_exporting()
#
#     def open_spider(self, spider):
#         print('爬虫开始了...')
#
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item
#
#     def close_spider(self, spider):  # 结束
#         self.exporter.finish_exporting()
#         self.fp.close()
#         print('爬虫结束了...')



'''最优版数据存储方式（注：要以二进制形式写入wb）'''
from scrapy.exporters import JsonLinesItemExporter

class QsbkPipeline(object):
    def __init__(self):
        self.fp = open("duanzi.json", 'wb')
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
        self.exporter.start_exporting()

    def open_spider(self, spider):
        print('爬虫开始了...')

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):  # 结束
        self.fp.close()
        print('爬虫结束了...')
