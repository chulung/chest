# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst


class TotalspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class LagouJobItem(scrapy.Item):
    title = scrapy.Field()
    salary = scrapy.Field()
    jobCity = scrapy.Field()
    workYears = scrapy.Field()
    degreeNeed = scrapy.Field()
    jobDesc = scrapy.Field()
    jobAdvantage = scrapy.Field()
    jobAddr = scrapy.Field()
    companyName = scrapy.Field()
    url = scrapy.Field()


class LagouJobItemLoader(ItemLoader):
    default_output_processor = TakeFirst()
