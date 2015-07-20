# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.selector import Selector
from tencent.items import TencentItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class TencentSpider(CrawlSpider):
    name = "TencentSpider"
    allowed_domains = ["v.qq.com"]
    start_urls = ["http://v.qq.com/rank/"]

    def parse(self, response):
        items =[]
        categories = response.xpath("//div[contains(@class, 'wrapper wrapper_rank')]")
        print(categories)
        for wrapper in categories:
            cate = self.get_category(wrapper)
            items += self.get_items(wrapper, cate)
        return items

    def get_category(self, response):
        return response.xpath(".//h2[@class ='rank_title']/span/text()").extract()[0]

    def get_items(self, response, cate):
        items =[]
        countries = response.xpath("./div[@class = 'mod_bd rank_lists']/ul/li[1]")
        for country in countries:
            country_name = country.xpath("./text()").extract()[0]
            for name in country.xpath("./following-sibling::li/a/@title").extract():
                item = TencentItem()
                item['rank_category'] = cate
                item['rank_country'] = country_name
                item['rank_name'] = name
                items.append(item)
        return items



