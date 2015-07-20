# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiboItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    rank_category = scrapy.Field()
    rank_name = scrapy.Field()
    rank__broad_time = scrapy.Field()
    rank_channel = scrapy.Field()
    rank_reader = scrapy.Field()
    rank_read_times = scrapy.Field()
    rank_mention = scrapy.Field()
    rank_mention_times = scrapy.Field()

