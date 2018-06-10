# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymysql import connect


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

    def save_dangdang(self, item):
        # 连接配置信息
        config = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': '123456',
            'db': 'python',
            'charset': 'utf8mb4', }
        # 创建连接
        conn = connect(**config)
        cus = conn.cursor()
        for i in range(len(item['title'])):
            title = item['title'][i]
            author = item['author'][i]
            link = item['link'][i]
            print("%s  %s  %s\n" % (title, author, link))

            sql = 'INSERT INTO dangdang (title,link,author) VALUES (%s, %s, %s)'
            values = (title, link, author)
            try:
                cus.execute(sql, values)  # execute 执行定义的 sql 变量语句
                conn.commit()  # 提交到数据库执行，注意此处是 数据库链接对象的 commit 方法，不是游标的方法
            except Exception as e:
                conn.rollback()  # 如果发生错误，先执行回滚操作
                print(e)
                raise e  # 如果发生错误，raise 错误并退出
        cus.close()
        conn.close()
