# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.selector import Selector
from baidu.items import BaiduItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class BaiduSpider_zy(CrawlSpider):
	name = 'BaiduSpider_zy'
	allowed_domains = ["top.baidu.com"]
	start_urls = ["http://top.baidu.com/buzz?b=19"]

	def parse(self, response):
		print response.url
		items =[]
		table = response.xpath('//div[class="mainBody"]')
		items += self.get_tab1(table)
		items += self.get_tab2(table)
		return items

	def get_tab1(self, response):
		items = []
		for rank in response.xpath('./div[@class="grayborder"]/table[@class="list-table"]/tbody/tr[@class="hideline"]'):
			item = BaiduItem()
			item['rank_category'] = 'zongyi'
			item['rank_name'] = rank.xpath('./td[@class="keyword"]/a[@class="list-title"]/text()').extract()
			item['rank_index'] = rank.xpath('./td[@class="last"]/span/text()').extract()
			items.append(item)
		return items

	def get_tab2(self, response):
		items = []
		for rank in response.xpath('./div[@class="grayborder"]/table[@class="list-table"]/tbody/tr[7]/following-sibling::tr'):
			item = BaiduItem()
			item['rank_category'] = 'zongyi'
			item['rank_name'] = rank.xpath('./td[@class="keyword"]/a[@class="list-title"]/text()').extract()
			item['rank_index'] = rank.xpath('./td[@class="last"]/span/text()').extract()
			items.append(item)
		return items




