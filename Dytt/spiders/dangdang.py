# -*- coding: utf-8 -*-
import scrapy
from Dytt.items import DDItem
from scrapy.http import Request


class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['dangdang.com/']
    # start_urls = [
    #     'http://www.dangdang.com',
    # ]

    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.5408.400 QQBrowser/10.1.1430.400",
    }

    def start_requests(self):
        for i in range(1, 9):
            url = 'http://book.dangdang.com/01.0%s.htm' % i
            yield Request(url=url, callback=self.parse, headers=self.header)

    def parse(self, response):
        item = DDItem()
        item["title"] = response.xpath("//li/a[@class='img']/@title").extract()
        item["link"] = response.xpath("//li/a[@class='img']/@href").extract()
        item["author"] = response.xpath("//p[@class='author']/text()").extract()
        yield item
