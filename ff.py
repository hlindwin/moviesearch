import json

import os
import scrapy
import datetime


class FfSpider(scrapy.Spider):
    name = 'ffspider'
    allowed_domains = ['www.focusfeatures.com/']
    start_urls = ['http://www.focusfeatures.com/films]

    def parse(self, response):
        print(response.url)
#what does yield do.  Why
        for url in response.xpath("//div[@id='Pator']/table/tr/td/span/a/@href").extract():
            yield scrapy.Request("https://www.fsite.com%s" % url, callback=self.parse)

        for url in response.xpath("//div[@class='relatedContainer']/a/@href").extract():
            yield scrapy.Request("https://www.fsite.com%s" % url, callback=self.parse)

        if not self.is_update(response):
            return

        name = self.file_name(response)
        print("%s - %s" % (name, response.url))

        description = response.xpath("//div[@id='desc']/p/text()").extract()


        with open(name, 'w+') as f:
            json.dump({'description': description[0], f)


        #with open(name, 'w+') as f:
        #    json.dump({'description': description, 'videos': videos, 'name': name, 'stats': stats}, f)

    def is_update(self, response):
        url = response.url
        first = 'https://www.fsite.com/update/'
        return url[0:len(first)] == first

    def file_name(self, response):

        data_path = os.path.normpath(os.path.join(os.getcwd(), 'data'))
        if not os.path.exists(data_path):
            os.makedirs(data_path)

        url = response.url
        last = url.rfind('/')
        file_name = "%s.json" % url[last + 1:-5]
        return os.path.join(data_path, file_name)


# # # ./venv/bin/python ./bin_crawler_ff.py
