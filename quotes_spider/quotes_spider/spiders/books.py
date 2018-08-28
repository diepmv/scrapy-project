# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class BooksSpider(CrawlSpider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    #rules = (Rule(LinkExtractor(deny_domains=('google.com')), callback='parge_page', follow=False),)
    rules = (Rule(LinkExtractor(allow='music'), callback='parge_page', follow=True),)


    def parse_page(self, response):
        yield {'URL': response.url}