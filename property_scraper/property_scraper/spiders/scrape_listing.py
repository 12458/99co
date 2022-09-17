# https://www.99.co/singapore/sale
# Regex to get listing ID from URL: (?<=\-)[^-]+(?=\#)
import scrapy
import re
import requests
import json


class PropertyScraper(scrapy.Spider):
    name = 'scrape_listing'

    def start_requests(self):
        with open('urls.txt') as f:
            urls = f.read().split('\n')
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        property_data = {}
        table = response.xpath('//*[@id="propertyDetails"]/table//tr')
        for tr in table:
            data = tr.xpath('div/td//text()').getall()
            for i in range(0, len(data), 2):
                property_data[data[i]] = data[i + 1]
        listing_id = re.findall('(?<=\-)[^-]+(?=\#)', response.request.url)[0]
        headers = {
                    "sec-ch-ua": "\"Google Chrome\";v=\"105\", \"Not)A;Brand\";v=\"8\", \"Chromium\";v=\"105\"",
                    "sec-ch-ua-mobile": "?0",
                    "sec-ch-ua-platform": "\"Linux\"",
                    "sec-fetch-dest": "empty",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-site": "same-origin",
                    "referrer": response.request.url,
                    "referrerPolicy": "strict-origin-when-cross-origin",
                    "mode": "cors",
                    "credentials": "include",
                    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
                }
        data = {
            "listing_id": listing_id,
            "get_phone": "true",
            "source": "web"
        } 
        r = requests.post('https://www.99.co/-/show-phone', json=data, headers=headers)
        phone_no = json.loads(r.text)['phone']
        yield {
            'id': listing_id,
            'title': response.xpath('//*[@id="overview"]/div/div[2]/div[1]/h1/text()').get(),
            'price': response.xpath('//*[@id="price"]/div/p/text()').get(),
            'property_details': property_data,
            'description': response.xpath('//*[@id="description"]/div/div/div/div/text()[1]/text()').get(),
            'agent':{'name': response.xpath('//*[@id="listingPageContent"]/div[2]/div/div/div/div/div[2]/a/p/text()').get(),'phone': phone_no},
            'scrape_link': response.request.url
            }