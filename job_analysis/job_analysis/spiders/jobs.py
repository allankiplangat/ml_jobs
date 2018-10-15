# -*- coding: utf-8 -*-
import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['www.glassdoor.com']
    start_urls = ['http://www.glassdoor.com/']

    def parse(self, response):
        pass
