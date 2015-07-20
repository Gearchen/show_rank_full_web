# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.selector import Selector
from Iqiyi.items import IqiyiItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class IqiyiSpider_dsj(CrawlSpider):
    name = 'IqiyiSpider_dsj'
    allowed_domains = ["top.iqiyi.com"]
    start_urls = ["http://top.iqiyi.com/dianshiju.html"]

    def parse(self, response):
        items = []
        category = response.url.strip().split('/')[-1][:-5]
        table = response.xpath('//div[@class="Ranking wb"]')
        items +=  self.get_tab1(table, category)
        return items

    def get_tab1(self, response, category):
        items =[]
        for rank in response.xpath('./div[@id="tab_top50"]/div[@j-tab-cnt="t1"]/ul/li'):
            item = IqiyiItem()
            item['rank_category'] =  category
            item['rank_name'] = rank.xpath('./a[@class="topic"]/@title').extract()
            item['rank_tag'] = rank.xpath('./span[@class="Actor"]/a/text()').extract()
            item['rank_7day'] = rank.xpath('./a[@class="Last_week"]/text()').extract()
            item['rank_yest'] = rank.xpath('./a[@class="Yesterday nolink"]/text()').extract()
            item['rank_hist'] = rank.xpath('./a[@class="history nolink"]/text()').extract()
            items.append(item)
        return items


class IqiyiSpider_zy_detail(CrawlSpider):
    name = 'IqiyiSpider_zy_detail'
    allowed_domains =["top.iqiyi.com"]
    start_urls = ['http://top.iqiyi.com/zongyi.html']

    def parse(self, response):
        items = []
        category = response.url.strip().split('/')[-1][:-5]
        table = response.xpath('//div[@class="Ranking wb"]')
        items +=  self.get_tab1(table, category)
        return items

    def get_tab1(self, response, category):
        items =[]
        for rank in response.xpath('./div[@id="tab_top50"]/div[@j-tab-cnt="t1"]/ul/li'):
            item = IqiyiItem()
            item['rank_category'] =  category
            item['rank_name'] = rank.xpath('./a[@class="topic"]/@title').extract()
            item['rank_tag'] = rank.xpath('./span[@class="Actor"]/a/text()').extract()
            item['rank_7day'] = rank.xpath('./a[@class="Last_week"]/text()').extract()
            item['rank_yest'] = rank.xpath('./a[@class="Yesterday"]/text()').extract()
            item['rank_hist'] = rank.xpath('./a[@class="history"]/text()').extract()
            items.append(item)
        return items

class IqiyiSpider_zy(CrawlSpider):
    name = 'IqiyiSpider_zy'
    allowed_domains =["top.iqiyi.com"]
    start_urls = ['http://top.iqiyi.com/zongyi.html']

    def parse(self, response):
        items = []
        category = response.url.strip().split('/')[-1][:-5]
        table = response.xpath('//div[@class="Ranking wb"]')
        items +=  self.get_tab1(table, category)
        return items

    def get_tab1(self, response, category):
        items =[]
        for rank in response.xpath('./div[@id="tab_top50"]/div[@j-tab-cnt="t2"]/ul/li'):
            item = IqiyiItem()
            item['rank_category'] =  category
            item['rank_name'] = rank.xpath('./a[@class="topic"]/@title').extract()
            #item['rank_tag'] = rank.xpath('./span[@class="Actor"]/a/text()').extract()
            item['rank_7day'] = rank.xpath('./a[@class="Last_week"]/text()').extract()
            item['rank_yest'] = rank.xpath('./a[@class="Yesterday"]/text()').extract()
            item['rank_hist'] = rank.xpath('./a[@class="history"]/text()').extract()
            items.append(item)
        return items


class IqiyiSpider_dy(CrawlSpider):
    name = 'IqiyiSpider_dy'
    allowed_domains =["top.iqiyi.com"]
    start_urls = ['http://top.iqiyi.com/dianying.html']

    def parse(self, response):
        items = []
        category = response.url.strip().split('/')[-1][:-5]
        table = response.xpath('//div[@class="Ranking wb"]')
        items +=  self.get_tab1(table, category)
        return items

    def get_tab1(self, response, category):
        items =[]
        for rank in response.xpath('./div[@id="tab_top50"]/div[@j-tab-cnt="t1"]/ul/li'):
            item = IqiyiItem()
            item['rank_category'] =  category
            item['rank_name'] = rank.xpath('./a[@class="topic"]/@title').extract()
            item['rank_tag'] = rank.xpath('./span[@class="Actor"]/a/text()').extract()
            item['rank_7day'] = rank.xpath('./a[@class="Last_week"]/text()').extract()
            item['rank_yest'] = rank.xpath('./a[@class="Yesterday nolink"]/text()').extract()
            item['rank_hist'] = rank.xpath('./a[@class="history nolink"]/text()').extract()
            items.append(item)
        return items


