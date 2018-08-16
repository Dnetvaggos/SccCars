# -*- coding: utf-8 -*-
import scrapy
from itertools import zip_longest

class SccbotSpider(scrapy.Spider):
    name = 'SccBot'
    start_urls = ['https://tinyurl.com/y8uhysda']

    def parse(self, response):
        content = response.css('div.content_boxes')
        model = content.css('tr.copy > td[colspan="1"] > a::text').extract()
        year = content.css('tr.copy > td[colspan="2"] > a::text').extract()
        type = content.css('tr.copy > td[colspan="3"] > a::text').extract()

        for item in zip_longest(model,year,type):
            scraped_info = {
            'model' : item[0],
            'year' : item[1],
            'type' : item[2],
            }
            yield scraped_info
