# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class IqiyiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank_media = scrapy.Field()
    rank_timestamp = scrapy.Field()
    rank_category = scrapy.Field()
    rank_kind = scrapy.Field()
    rank_name = scrapy.Field()
    rank_tag = scrapy.Field()
    rank_7day = scrapy.Field()
    rank_yest = scrapy.Field()
    rank_hist = scrapy.Field()


