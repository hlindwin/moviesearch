import scrapy
from scrapy.crawler import CrawlerProcess

from ff import FfSpider


process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'DOWNLOAD_DELAY': 3,
})

process.crawl(FfSpider)
process.start() # the script will block here until the crawling is finished
