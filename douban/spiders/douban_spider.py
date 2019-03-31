# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem

class DoubanSpiderSpider(scrapy.Spider):
    #爬虫名称
    name = "douban_spider"
    #允许域名
    allowed_domains = ["movie.douban.com"]
    #入口url，扔到调度器里
    start_urls = ['https://movie.douban.com/top250']
    #默认解析方法
    def parse(self, response):
    	movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
    	#循环电影条目
    	for i_item in movie_list:
    	    #导入i_item文件
        	douban_item = DoubanItem()
        	#进行每一项数据解析
        	douban_item['serial_number'] = i_item.xpath(".//div[@class='item']//em/text()").extract_first()
        	douban_item['movie_name'] = i_item.xpath(".//div[@class='info']//div[@class='hd']/a/span[1]/text()").extract_first()
        	content = i_item.xpath(".//div[@class='info']//div[@class='bd']/p[1]/text()").extract()
        	#处理多行数据时，合为一条信息
        	for i_content in content:
        		#去除空格连成一句话，“”.join表示不间隔连接 （PS：“-”.join(list['1','2','3'])-->“1-2-3”）
        		content_s="".join(i_content.split())
        		douban_item['introduce'] = content_s
        		#print(douban_item)#查看解析情况，cmd运行输出
        	douban_item['star'] = i_item.xpath(".//div[@class='info']//div[@class='bd']//div[@class='star']/span[2]/text()").extract_first()
        	douban_item['evaluate'] = i_item.xpath(".//div[@class='info']//div[@class='bd']//div[@class='star']/span[4]/text()").extract_first()
        	douban_item['disceibe'] = i_item.xpath(".//div[@class='info']//div[@class='bd']//p[@class='quote']/span/text()").extract_first()
        	#上交数据到pipelines里，进行下一步数据清洗、存储
        	yield douban_item
        #解析下一页，获取下一页xpath
    	next_link = response.xpath("//span[@class='next']/link/@href").extract()
    	if next_link:
    		next_link = next_link[0]
    		yield scrapy.requests("https://movie.douban.com/top250"+next_link,callback=self.parse)
