# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShgoldItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 日期
    data = scrapy.Field()
    #合约
    contract = scrapy.Field()
    #开盘价
    Opening_price = scrapy.Field()
    #最高价
    Highest_price = scrapy.Field()
    #最低价
    Minimum_price = scrapy.Field()
    #收盘价
    Closing_price = scrapy.Field()
    #涨跌
    Change = scrapy.Field()
    #涨跌幅
    Chg = scrapy.Field()
    #加权平均价
    VWAP = scrapy.Field()
    #成交量
    Volume = scrapy.Field()
    #成交金额
    Turnover = scrapy.Field()

