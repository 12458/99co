# https://www.99.co/singapore/sale
# User agent: Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1
# response.css('div._2kH6B a::attr(href)').get()

import scrapy


class PropertyScraper(scrapy.Spider):
    name = 'scrape_urls'

    def start_requests(self):
        urls = [
            'https://www.99.co/singapore/sale'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers={'User-Agent':'Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'})

    def parse(self, response):
        yield {
            'urls':[response.urljoin(i) for i in response.css('div._2kH6B a::attr(href)').getall()],
            'scrape_link': response.request.url
            }

        next_page = response.css('a.ytz-8::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse, headers={'User-Agent':'Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'})