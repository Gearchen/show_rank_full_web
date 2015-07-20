# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.selector import Selector
from youku.items import YoukuItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

class youkuSpider_dsj(CrawlSpider):
	name = 'youkuSpider_dsj'
	allowed_domains = ["index.youku.com"]
	start_urls = ["http://index.youku.com/protop/0"]

	def parse(self, response):
		items =[]
		table = response.xpath('//div[@class="rankall"]')
		items += self.get_tab1(table)
		return items

	def get_tab1(self,response):
		items =[]
		for rank in response.xpath('./div[@class="rank"]/table/tbody/tr'):
			item = YoukuItem()
			item['rank_category'] = 'dianshiju'
			item['rank_name'] = rank.xpath('./td[@class="key"]/a/@title').extract()
			item['rank_actor'] = rank.xpath('./td[@class="intro"]/a/text()').extract()
			item['rank_index'] = rank.xpath('./td[@class="status"]/span/a/text()').extract()
			item['rank_trend'] = rank.xpath('./td[@class="trend"]/span/@class').extract()
			items.append(item)
		return items

class youkuSpider_zy(CrawlSpider):
	name = 'youkuSpider_zy'
	allowed_domains = ["index.youku.com"]
	start_urls = ["http://index.youku.com/protop/1"]

	def parse(self, response):
		items =[]
		table = response.xpath('//div[@class="rankall"]')
		items += self.get_tab1(table)
		return items

	def get_tab1(self,response):
		items =[]
		for rank in response.xpath('./div[@class="rank"]/table/tbody/tr'):
			item = YoukuItem()
			item['rank_category'] = 'zongyi'
			item['rank_name'] = rank.xpath('./td[@class="key"]/a/@title').extract()
			item['rank_actor'] = rank.xpath('./td[@class="intro"]/a/text()').extract()
			item['rank_index'] = rank.xpath('./td[@class="status"]/span/a/text()').extract()
			item['rank_trend'] = rank.xpath('./td[@class="trend"]/span/@class').extract()
			items.append(item)
		return items

class youkuSpider_dy(CrawlSpider):
	name = 'youkuSpider_dy'
	allowed_domains = ["index.youku.com"]
	start_urls = ["http://index.youku.com/protop/2"]

	def parse(self, response):
		items =[]
		table = response.xpath('//div[@class="rankall"]')
		items += self.get_tab1(table)
		return items

	def get_tab1(self,response):
		items =[]
		for rank in response.xpath('./div[@class="rank"]/table/tbody/tr'):
			item = YoukuItem()
			item['rank_category'] = 'dianying'
			item['rank_name'] = rank.xpath('./td[@class="key"]/a/@title').extract()
			item['rank_actor'] = rank.xpath('./td[@class="intro"]/a/text()').extract()
			item['rank_index'] = rank.xpath('./td[@class="status"]/span/a/text()').extract()
			item['rank_trend'] = rank.xpath('./td[@class="trend"]/span/@class').extract()
			items.append(item)
		return items



