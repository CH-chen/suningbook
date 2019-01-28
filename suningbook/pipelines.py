# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json,codecs
from scrapy.exceptions import DropItem
#第一种要在settings中配置保存路径  SUNING_FILE_PATH="suningdata.log"
#两个piplines的执行顺序，根据权重，先打开第一个，后打开第二个，先执行第一个，后执行第二个，先关闭第二个，后关闭第一个
class SuningbookPipeline(object):
    def __init__(self,path):
        self.f = None
        self.path = path

    @classmethod
    def from_crawler(cls, crawler):
        """
        初始化时候，用于创建pipeline对象
        :param crawler:
        :return:
        """
        print('File.from_crawler')
        #去所有的配置文件中找SUNING_FILE_PATH
        path = crawler.settings.get('SUNING_FILE_PATH')
        return cls(path)

    def open_spider(self,spider):
        """
        爬虫开始执行时，调用
        :param spider:
        :return:
        """
        # if spider.name == 'chouti':#多个爬虫项目时，执行chouti的pipelines
        print('File.open_spider')
        self.f = open(self.path,'a+',encoding='utf-8')

    def process_item(self, item, spider):
        # f = open('xx.log','a+')
        # f.write(item['href']+'\n')
        # f.close()
        lines = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.f.write(lines)
        return item #这个return item 的作用是交给下一个pipeliens里面的process_item的item,
                    # 如果没有return下一个pipelines不会接收到值，为空
        # raise DropItem() #如果不想让下面的pipelines的process_item执行，可以不用return item 用这个raise DropItem，抛出异常


    def close_spider(self,spider):
        """
        爬虫关闭时，被调用
        :param spider:
        :return:
        """
        print('File.close_spider')
        self.f.close()
#可以设置两个pipelines ,一个保存到文件，一个保存到数据库
# class DbSuningbookPipeline(object):
#     def __init__(self,path):
#         self.f = None
#         self.path = path
#
#     @classmethod
#     def from_crawler(cls, crawler):
#         """
#         初始化时候，用于创建pipeline对象
#         :param crawler:
#         :return:
#         """
#         print('File.from_crawler')
#         #去所有的配置文件中找SUNING_FILE_PATH
#         path = crawler.settings.get('SUNING_FILE_PATH')
#         return cls(path)
#
#     def open_spider(self,spider):
#         """
#         爬虫开始执行时，调用
#         :param spider:
#         :return:
#         """
#         # if spider.name == 'chouti':
#         print('File.open_spider')
#         self.f = open(self.path,'a+',encoding='utf-8')
#
#     def process_item(self, item, spider):
#         # f = open('xx.log','a+')
#         # f.write(item['href']+'\n')
#         # f.close()
#         lines = json.dumps(dict(item), ensure_ascii=False) + "\n"
#         self.f.write(lines)
#         return item
#
#
#     def close_spider(self,spider):
#         """
#         爬虫关闭时，被调用
#         :param spider:
#         :return:
#         """
#         print('File.close_spider')
#         self.f.close()
#第二种
# class SuningbookPipeline(object):
#     """
#     将数据保存到json文件，由于文件编码问题太多，这里用codecs打开，可以避免很多编码异常问题
#         在类加载时候自动打开文件，制定名称、打开类型(只读)，编码
#         重载process_item，将item写入json文件，由于json.dumps处理的是dict，所以这里要把item转为dict
#         为了避免编码问题，这里还要把ensure_ascii设置为false，最后将item返回回去，因为其他类可能要用到
#         调用spider_closed信号量，当爬虫关闭时候，关闭文件
#     """
#     def __init__(self):
#         self.file = codecs.open('suning.json', 'w', encoding="utf-8")
#
#     def process_item(self, item, spider):
#         lines = json.dumps(dict(item), ensure_ascii=False) + "\n"
#         ## 注意需要有一个参数ensure_ascii=False ，不然数据会直接为utf编码的方式存入比如:“/xe15”
#         self.file.write(lines)
#         return item
#
#     def spider_closed(self, spider):
#         self.file.close()


#第三种
# class SuningbookPipeline(object):
#     def open_spider(self,spider):
#         self.f = open('xxx.text','a+',encoding='utf-8')
#
#     def process_item(self, item, spider):
#         # print(item)
#         line = json.dumps(dict(item), ensure_ascii=False) + "\n"
#         self.f.write(line)
#         return item
#
#     def close_spider(self,spider):
#         self.f.close()

# #第四种
# class SuningbookPipeline(object):
#     def process_item(self, item, spider):
#
#         with open('data.txt', 'a') as f:
#             f.write(item['title_1'])
#             f.write(item['href_1'])
#             f.write(item['book_name'] + '\n')
#         return item

