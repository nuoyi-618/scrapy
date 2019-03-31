# -*- coding: utf-8 -*-
import scrapy
from SHgold.items import ShgoldItem

class ShgoldSpiderSpider(scrapy.Spider):
    name = "SHgold_spider"
    allowed_domains = ["www.sge.com.cn"]
    url = "https://www.sge.com.cn/sjzx/mrhqsj"
    start_urls = ['https://www.sge.com.cn/sjzx/mrhqsj']
    def parse(self, response):
        url_list = response.xpath("//div[@class='articleList border_ea mt30 mb30']//a/@href").extract()
        for url in url_list:
            yield scrapy.Request("https://www.sge.com.cn/"+url,callback=self.parse_gold)
        for i in range(2,5):
            yield scrapy.Request("https://www.sge.com.cn/sjzx/mrhqsj?p="+i,callback=self.parse)
    def parse_gold(self,response):
        gold_list = response.xpath("//table//tr")
        data_item = response.xpath("//div[@class='title']/p/span[2]/text()").extract()
        for i_item in range(1,len(gold_list)):
            SHgold_item = ShgoldItem()
            SHgold_item['data'] =data_item[0].split()
            SHgold_item['contract'] = gold_list[i_item].xpath("./td[1]/text()").extract_first().split()
            SHgold_item['Opening_price'] = gold_list[i_item].xpath("./td[2]/text()").extract_first().split()
            SHgold_item['Highest_price'] = gold_list[i_item].xpath("./td[3]/text()").extract_first().split()
            SHgold_item['Minimum_price'] = gold_list[i_item].xpath("./td[4]/text()").extract_first().split()
            SHgold_item['Closing_price'] = gold_list[i_item].xpath("./td[5]/text()").extract_first().split()
            SHgold_item['Change'] = gold_list[i_item].xpath("./td[6]/text()").extract_first().split()
            SHgold_item['Chg'] = gold_list[i_item].xpath("./td[7]/text()").extract_first().split()
            SHgold_item['VWAP'] = gold_list[i_item].xpath("./td[8]/text()").extract_first().split()
            SHgold_item['Volume'] = gold_list[i_item].xpath("./td[9]/text()").extract_first().split()
            SHgold_item['Turnover'] = gold_list[i_item].xpath("./td[10]/text()").extract_first().split()               
            print(SHgold_item)
            yield SHgold_item






