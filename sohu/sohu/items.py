# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SohuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank_category = scrapy.Field()
    rank_name = scrapy.Field()
    rank_type = scrapy.Field()
    rank_index = scrapy.Field()
    rank_trend = scrapy.Field()