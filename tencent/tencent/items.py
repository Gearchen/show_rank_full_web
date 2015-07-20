# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    rank_category = scrapy.Field()
    rank_country = scrapy.Field()
    rank_name = scrapy.Field()

