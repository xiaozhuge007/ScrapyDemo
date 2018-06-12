# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymysql import connect
from Dytt.sql.SqlHelper import Sql


class DyttPipeline(object):

    def process_item(self, item, spider):
        if spider.name == 'dytt':
            self.save_dytt(item)
        elif spider.name == 'dangdang':
            self.save_dangdang(item)
        return item

    def save_dytt(self, item):
        for i in range(len(item['name'])):
            name = item['name'][i]
            down = item['down'][i]
            print(name)
            print(down)
            if str(down).startswith("ftp:"):
                Sql.insert_dytt(name, down)

    def save_dangdang(self, item):
        for i in range(len(item['title'])):
            title = item['title'][i]
            author = item['author'][i]
            link = item['link'][i]
            print("%s  %s  %s\n" % (title, author, link))

            Sql.insert_dangdang(title, author, link)
