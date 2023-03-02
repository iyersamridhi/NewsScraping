import scrapy
import pandas as pd


class QuotesSpider(scrapy.Spider):
    name = "datapars"
    url_label = None

    def start_requests(self):
        urls = [
            "https://www.hindustantimes.com/entertainment",
            "https://www.hindustantimes.com/cricket",
            "https://www.hindustantimes.com/india-news"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        print("Name in start_request: ")
        print(self.name)

    def parse(self, response):
        data = response.selector.xpath('//h3[@class="hdg3"]//a/@href').extract()
        # print("Data extracted: ", data)
        list_ht = []
        for link in data:
            sub_url = "https://www.hindustantimes.com" + link
            # print(sub_url)
            list_ht.append(sub_url)
        print(list_ht)
        print("Name from parse: ")
        print(self.name)
        for url in list_ht:
            yield scrapy.Request(url=url, callback=self.data_collector, meta={'url': url})
            # df['url'] = url


    def data_collector(self, response):
        title = response.selector.xpath('//h1[@class="hdg1"]/text()').extract()
        content = response.selector.xpath('//h2[@class = "sortDec"]/text()').extract()
        url = response.meta['url']

        samp = {
            'title': title,
            'description': content,
            'url': response.meta['url'],
        }
        print("\n #####  Dic of the netore news: ", samp)
        # print("\n\n Data Frame of the information: \n", data_df)
        print("Name from dta_collector")
        print("\n URKKKK :  ", self.url_label)
        yield samp











