import scrapy
from scrapy_heroku_redis_tutorial import items


class WikipediaSpider(scrapy.Spider):
    name = "wikipedia_featured_picture"
    allowed_domains = ["wikipedia.org"]
    start_urls = [
        "https://en.wikipedia.org/wiki/Main_Page"
    ]

    def parse(self, response):

        item = items.FeaturedPictureItem()
        item['url'] = "https:" + response.xpath('//div[@id="mp-tfp"]//a[@class="image"]//img//@src').extract()[0]
        item['description'] = response.xpath('normalize-space(//div[@id="mp-tfp"]//p)').extract()[0]
        yield item