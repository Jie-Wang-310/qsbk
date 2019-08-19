# -*- coding: utf-8 -*-
import scrapy
from qsbk.items import QsbkItem
from scrapy.http import Request


class MainSpider(scrapy.Spider):
    name = 'main'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']
    base_url = 'https://qiushibaike.com'

    def parse(self, response):
        item = QsbkItem()
        contents = response.xpath('//div[@id="content-left"]/div')  # 此方法是总内容下，各个div标签的内容
        for content in contents:
            author_name = content.xpath('.//h2/text()').getall()
            DZ_content = content.xpath('.//div[@class="content"]/span/text()').getall()
            DZ_content = "".join(DZ_content).strip()   # 将列表转为字符串并去除空白 要使用此方法必须用getall方法提取

            item['author_name'] = author_name
            item['DZ_content'] = DZ_content

            yield item

            nextlink = response.xpath('//ul[@class="pagination"]/li[last()]/a/@href').get()

            if not nextlink:
                return
            else:
                yield scrapy.Request(self.base_url + nextlink, callback=self.parse)


