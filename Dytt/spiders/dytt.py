# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Dytt.items import DyttItem


class DyttSpider(CrawlSpider):
    name = 'dytt'
    allowed_domains = ['www.dytt8.net']
    start_urls = ['http://www.dytt8.net']

    header = {

    }

    rules = (
        Rule(LinkExtractor(allow=r'gndy/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        i = DyttItem()
        i['name'] = response.xpath('//div[@class="title_all"]/h1/font/text()').extract()[0]
        # i['down'] = response.xpath("//div[@id='Zoom']/span/p/a/@href").extract()
        i['down'] = response.xpath("//table/tbody/tr/td/a/@href").extract()[0]
        print(i['name'] + "---" + i['down'])
        return i
