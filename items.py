import scrapy

class MycrawlerItem(scrapy.Item):
    title = scrapy.Field()
    url = scrapy.Field()

