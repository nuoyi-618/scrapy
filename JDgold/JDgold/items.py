# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdgoldItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()#品牌
    price = scrapy.Field()#价格
#    comment_num= scrapy.Field()#评价
    url = scrapy.Field()  # 商品链接
    brand = scrapy.Field()  # 品牌
    shop = scrapy.Field()#店铺


