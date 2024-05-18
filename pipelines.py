class MycrawlerPipeline:
    def process_item(self, item, spider):
        print(f"Scraped data: {item['title']} ({item['url']})")
        return item
