# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Dytt.items import DyttItem


class DyttSpider(CrawlSpider):
    name = 'dytt'
    allowed_domains = ['www.dytt8.net']
    start_urls = ['http://www.dytt8.net']

    rules = (
        Rule(LinkExtractor(allow=r'gndy/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = DyttItem()
        i['name'] = response.xpath('//div[@class="title_all"]/h1/font/text()').extract()
        # i['down'] = response.xpath('//div[@id="Zoom"]/span/p/a').extract()
        i['down'] = response.css('div#Zoom span p a::attr("href")').extract()
        print(i['down'])
        return i
