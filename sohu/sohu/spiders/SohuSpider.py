import scrapy
import re
from scrapy.selector import Selector
from sohu.items import SohuItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

#zongyi 
class Sohu_zy_day(CrawlSpider):
	name = 'Sohu_zy_day'
	allowed_domains = ['tv.sohu.com']
	start_urls = ["http://tv.sohu.com/hotshow/"]

	def parse(self, response):
		items = []
		category = response.url.strip().split('/')[-2]
		table = response.xpath('//div[@class="rList_con r_show r_show_jm"]/div[2]')
		items.append(self.get_tab1(table, category))
		items += self.get_tab(table, category)
		return items

	def get_tab1(self,response, category):
		item = SohuItem()
		item['rank_category'] = category
		item['rank_name'] = response.xpath('./ul[@class="rList"]/li[@class="No1"]/div[@class="cfix"]/div[@class="vName"]/a/@title').extract()
		item['rank_type'] = response.xpath('./ul[@class="rList"]/li[@class="No1"]/div[@class="cfix"]/span[@class="vSort"]/a/text()').extract()
		item['rank_index'] = response.xpath('./ul[@class="rList"]/li[@class="No1"]/div[@class="cfix"]/span[@class="vTotal"]/text()').extract()
		item['rank_trend'] = response.xpath('./ul[@class="rList"]/li[@class="No1"]/div[@class="cfix"]/span[@class="vRank"]/@title').extract()
		return item

	def get_tab(self, response, category):
		items =[]
		for group in response.xpath('./ul[@class="rList"]'):
			for rank in group.xpath('./li'):
				item = SohuItem()
				item['rank_category'] = category
				item['rank_name'] = rank.xpath('./div[@class="vName"]/div/a/text()').extract()
				item['rank_type'] = rank.xpath('./span[@class="vSort"]/a/text()').extract()
				item['rank_index'] = rank.xpath('./span[@class="vTotal"]/text()').extract()
				item['rank_trend'] = rank.xpath('./span[@class="vRank"]/@title').extract()
				items.append(item)
		return items


class Sohu_zy_week(CrawlSpider):
	name = 'Sohu_zy_week'
	allowed_domains = ['tv.sohu.com']
	start_urls = ["http://tv.sohu.com/hotshow/"]

	def parse(self, response):
		items = []
		category = response.url.strip().split('/')[-2]
		table = response.xpath('//div[@class="rList_con r_show r_show_jm"]/div[3]')
		items.append(self.get_tab1(table, category))
		items += self.get_tab(table, category)
		return items

	def get_tab1(self,response, category):
		item = SohuItem()
		item['rank_category'] = category
		item['rank_name'] = response.xpath('./ul[@class="rList"]/li[@class="No1"]/div[@class="cfix"]/div[@class="vName"]/a/@title').extract()
		item['rank_type'] = response.xpath('./ul[@class="rList"]/li[@class="No1"]/div[@class="cfix"]/span[@class="vSort"]/a/text()').extract()
		item['rank_index'] = response.xpath('./ul[@class="rList"]/li[@class="No1"]/div[@class="cfix"]/span[@class="vTotal"]/text()').extract()
		item['rank_trend'] = response.xpath('./ul[@class="rList"]/li[@class="No1"]/div[@class="cfix"]/span[@class="vRank"]/@title').extract()
		return item

	def get_tab(self, response, category):
		items =[]
		for group in response.xpath('./ul[@class="rList"]'):
			for rank in group.xpath('./li'):
				item = SohuItem()
				item['rank_category'] = category
				item['rank_name'] = rank.xpath('./div[@class="vName"]/div/a/text()').extract()
				item['rank_type'] = rank.xpath('./span[@class="vSort"]/a/text()').extract()
				item['rank_index'] = rank.xpath('./span[@class="vTotal"]/text()').extract()
				item['rank_trend'] = rank.xpath('./span[@class="vRank"]/@title').extract()
				items.append(item)
		return items

class Sohu_zy_month(CrawlSpider):
	name = 'Sohu_zy_month'
	allowed_domains = ['tv.sohu.com']
	start_urls = ["http://tv.sohu.com/hotshow/"]

	def parse(self, response):
		items = []
		category = response.url.strip().split('/')[-2]
		table = response.xpath('//div[@class="rList_con r_show r_show_jm"]/div[4]')
		items.append(self.get_tab1(table, category))
		items += self.get_tab(table, category)
		return items

	def get_tab1(self,response, category):
		item = SohuItem()
		item['rank_category'] = category
		item['rank_name'] = response.xpath('./ul[@class="rList"]/li[@class="No1"]/div[@class="cfix"]/div[@class="vName"]/a/@title').extract()
		item['rank_type'] = response.xpath('./ul[@class="rList"]/li[@class="No1"]/div[@class="cfix"]/span[@class="vSort"]/a/text()').extract()
		item['rank_index'] = response.xpath('./ul[@class="rList"]/li[@class="No1"]/div[@class="cfix"]/span[@class="vTotal"]/text()').extract()
		item['rank_trend'] = response.xpath('./ul[@class="rList"]/li[@class="No1"]/div[@class="cfix"]/span[@class="vRank"]/@title').extract()
		return item

	def get_tab(self, response, category):
		items =[]
		for group in response.xpath('./ul[@class="rList"]'):
			for rank in group.xpath('./li'):
				item = SohuItem()
				item['rank_category'] = category
				item['rank_name'] = rank.xpath('./div[@class="vName"]/div/a/text()').extract()
				item['rank_type'] = rank.xpath('./span[@class="vSort"]/a/text()').extract()
				item['rank_index'] = rank.xpath('./span[@class="vTotal"]/text()').extract()
				item['rank_trend'] = rank.xpath('./span[@class="vRank"]/@title').extract()
				items.append(item)
		return items

class Sohu_zy_all(CrawlSpider):
	name = 'Sohu_zy_all'
	allowed_domains = ['tv.sohu.com']
	start_urls = ["http://tv.sohu.com/hotshow/"]

	def parse(self, response):
		items = []
		category = response.url.strip().split('/')[-2]
		table = response.xpath('//div[@class="rList_con r_show r_show_jm"]/div[5]')
		items.append(self.get_tab1(table, category))
		items += self.get_tab(table, category)
		return items

	def get_tab1(self,response, category):
		item = SohuItem()
		item['rank_category'] = category
		item['rank_name'] = response.xpath('./ul[@class="rList"]/li[@class="No1"]/div[@class="cfix"]/div[@class="vName"]/a/@title').extract()
		item['rank_type'] = response.xpath('./ul[@class="rList"]/li[@class="No1"]/div[@class="cfix"]/span[@class="vSort"]/a/text()').extract()
		item['rank_index'] = response.xpath('./ul[@class="rList"]/li[@class="No1"]/div[@class="cfix"]/span[@class="vTotal"]/text()').extract()
		item['rank_trend'] = response.xpath('./ul[@class="rList"]/li[@class="No1"]/div[@class="cfix"]/span[@class="vRank"]/@title').extract()
		return item

	def get_tab(self, response, category):
		items =[]
		for group in response.xpath('./ul[@class="rList"]'):
			for rank in group.xpath('./li'):
				item = SohuItem()
				item['rank_category'] = category
				item['rank_name'] = rank.xpath('./div[@class="vName"]/div/a/text()').extract()
				item['rank_type'] = rank.xpath('./span[@class="vSort"]/a/text()').extract()
				item['rank_index'] = rank.xpath('./span[@class="vTotal"]/text()').extract()
				item['rank_trend'] = rank.xpath('./span[@class="vRank"]/@title').extract()
				items.append(item)
		return items

# movie
class Sohu_movie_day(CrawlSpider):
	name = 'Sohu_movie_day'
	allowed_domains = ['tv.sohu.com']
	start_urls = ["http://tv.sohu.com/hotmovie/"]

	def parse(self, response):
		items = []
		category = response.url.strip().split('/')[-2]
		table = response.xpath('//div[@class="rList_con r_movie"]/div[2]')
		items.append(self.get_tab1(table, category))
		items += self.get_tab(table, category)
		return items

	def get_tab1(self,response, category):
		item = SohuItem()
		item['rank_category'] = category
		item['rank_name'] = response.xpath('./ul[@class="rList"]/li[@class="No1"]/div[@class="cfix"]/div[@class="vName"]/a/@title').extract()
		item['rank_type'] = response.xpath('./ul[@class="rList"]/li[@class="No1"]/div[@class="cfix"]/span[@class="vStar"]/a/text()').extract()
		item['rank_index'] = response.xpath('./ul[@class="rList"]/li[@class="No1"]/div[@class="cfix"]/span[@class="vTotal"]/text()').extract()
		item['rank_trend'] = response.xpath('./ul[@class="rList"]/li[@class="No1"]/div[@class="cfix"]/span[@class="vRank"]/@title').extract()
		return item

	def get_tab(self, response, category):
		items =[]
		for group in response.xpath('./ul[@class="rList"]'):
			for rank in group.xpath('./li'):
				item = SohuItem()
				item['rank_category'] = category
				item['rank_name'] = rank.xpath('./div[@class="vName"]/div/a/text()').extract()
				item['rank_type'] = rank.xpath('./span[@class="vStar"]/a/text()').extract()
				item['rank_index'] = rank.xpath('./span[@class="vTotal"]/text()').extract()
				item['rank_trend'] = rank.xpath('./span[@class="vRank"]/@title').extract()
				items.append(item)
		return items

# dianshiju 
class Sohu_dianshiju_day(CrawlSpider):
	name = 'Sohu_dianshiju_day'
	allowed_domains = ['tv.sohu.com']
	start_urls = ["http://tv.sohu.com/hotdrama/"]

	def parse(self, response):
		items = []
		category = response.url.strip().split('/')[-2]
		table = response.xpath('//div[@class="rList_con r_drama r_drama_all"]/div[2]')
		items.append(self.get_tab1(table, category))
		items += self.get_tab(table, category)
		return items

	def get_tab1(self,response, category):
		item = SohuItem()
		item['rank_category'] = category
		item['rank_name'] = response.xpath('./ul[@class="rList"]/li[@class="No1"]/div[@class="cfix"]/div[@class="vName"]/a/@title').extract()
		item['rank_type'] = response.xpath('./ul[@class="rList"]/li[@class="No1"]/div[@class="cfix"]/span[@class="vStar"]/a/text()').extract()
		item['rank_index'] = response.xpath('./ul[@class="rList"]/li[@class="No1"]/div[@class="cfix"]/span[@class="vTotal"]/text()').extract()
		item['rank_trend'] = response.xpath('./ul[@class="rList"]/li[@class="No1"]/div[@class="cfix"]/span[@class="vRank"]/@title').extract()
		return item

	def get_tab(self, response, category):
		items =[]
		for group in response.xpath('./ul[@class="rList"]'):
			for rank in group.xpath('./li'):
				item = SohuItem()
				item['rank_category'] = category
				item['rank_name'] = rank.xpath('./div[@class="vName"]/div/a/text()').extract()
				item['rank_type'] = rank.xpath('./span[@class="vStar"]/a/text()').extract()
				item['rank_index'] = rank.xpath('./span[@class="vTotal"]/text()').extract()
				item['rank_trend'] = rank.xpath('./span[@class="vRank"]/@title').extract()
				items.append(item)
		return items















