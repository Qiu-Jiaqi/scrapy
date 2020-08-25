# -*- coding: utf-8 -*-
import scrapy
import json
from taptap.items import DownloadItem
from taptap.items import NewItem
from taptap.items import ReserveItem
from taptap.items import SellItem
from taptap.items import PlayedItem
from bs4 import BeautifulSoup


# 排行榜五个，暂时没用
# 合在一起使用parse_detail的方法会数据丢失，找不到原因，尝试过深拷贝，解决不了，该类拆分成了五个类。
# 使用未注释的方法仅获取三个tag
class RatingSpider(scrapy.Spider):
    name = 'rating'
    allowed_domains = ['www.taptap.com']
    start_urls = ['https://www.taptap.com/ajax/top/download?total=0&page=1',
                  'https://www.taptap.com/ajax/top/new?total=0&page=1',
                  'https://www.taptap.com/ajax/top/reserve?total=0&page=1',
                  'https://www.taptap.com/ajax/top/sell?total=0&page=1',
                  'https://www.taptap.com/ajax/top/played?total=0&page=1'
                  ]

    def parse(self, response):
        print(response.url)
        datas = json.loads(response.body)
        soup = BeautifulSoup(datas['data']['html'], 'lxml')
        for card in soup.select('body > div'):
            type = response.url.split('/')[-1].split('?')[0]
            if type == 'download':
                item = DownloadItem()
            elif type == 'new':
                item = NewItem()
            elif type == 'reserve':
                item = ReserveItem()
            elif type == 'sell':
                item = SellItem()
            elif type == 'played':
                item = PlayedItem()
            item['top'] = card.select("span.top-card-order-text")[0].get_text()
            item['id'] = card.select("div.top-card-middle > a")[0].get('href').split('/')[-1]
            item['name'] = card.select('div.top-card-middle > a > h4')[0].get_text().replace('CN', '').strip()
            item['author'] = card.select('div.top-card-middle > p.card-middle-author > a')[0].get_text() \
                .split('\xa0')[-1]
            rating = card.select('div.top-card-middle > div.card-middle-score > p > span')
            item['rating'] = "评分过少"
            if rating:
                item['rating'] = rating[0].get_text()
            tags = []
            for tag in card.select('div.top-card-middle > div.card-tags > a.btn.btn-xs.btn-default'):
                tags.append(tag.get_text())
            item['tags'] = ",".join(tags)
            item['category'] = card.select('div.top-card-middle > div.card-middle-category > a')[
                0].get_text()
            yield item
        # params = {
        #     'page': self.page + 1,
        #     'total': 30 * self.page
        # }
        # next_url = 'https://www.taptap.com/ajax/top/download?' + urlencode(params)
        next_url = datas['data']['next']
        if next_url:
            yield scrapy.Request(next_url)

    # 下面方法进入详细页获取，不知道为什么爬取数据不完整，异步插入问题，但是使用了深拷贝也没解决
    #     datas = json.loads(response.body)
    #     soup = BeautifulSoup(datas['data']['html'], 'lxml')
    #     for card in soup.select('body > div'):
    #         item = DownloadItem()
    #         item['top'] = card.select("span.top-card-order-text")[0].get_text()  # top
    #         yield scrapy.Request(card.select('div.top-card-middle > a')[0].get('href'), self.parse_detail,
    #                              meta={'item': item})
    #     next_url = datas['data']['next']
    #     if next_url:
    #         yield scrapy.Request(next_url)

    # def parse_detail(self, response):
    #     print(response.url)
    #     item = response.meta['item']
    #     item['id'] = response.url.split('/')[-1]
    #     item['name'] = response.xpath(
    #         '//*[@id="js-nav-sidebar-main"]/div[1]/div/div/section[1]/div[1]/div[2]/div[1]/h1/text()'). \
    #         extract()[0].strip()
    #     item['author'] = response.xpath(
    #         '//*[@id="js-nav-sidebar-main"]/div[1]/div/div/section[1]/div[1]/div[2]/div[1]/div/a/span[2]/text()'). \
    #         extract()[0].strip()
    #     rating = response.xpath(
    #         '//*[@id="js-nav-sidebar-main"]/div[1]/div/div/section[1]/div[1]/div[2]/div[1]/span/span/span/text()')
    #     if rating:
    #         item['rating'] = rating.extract()[0]
    #     else:
    #         item['rating'] = "评分过少"
    #     tags = []
    #     for sel in response.xpath('//*[@id="appTag"]/li'):
    #         tag = sel.xpath('a/text()')
    #         if tag:
    #             tags.append(tag.extract()[0].strip())
    #     item['tags'] = ",".join(tags)
    #     item['category'] = \
    #         response.xpath('//*[@id="js-nav-sidebar-main"]/section[1]/div/div/ol/li[3]/a/text()').extract()[0]
    #     yield item

# 使用 https://www.taptap.com/top/download 源网址数据爬取，因翻页后格式变为json不一致，废
# for sel in response.xpath('//*[@id="topList"]/div'):
#     print(sel)
#     item = TaptapItem()
#     item['top'] = int(sel.xpath('span[2]/text()').extract()[0])
#     item['name'] = sel.xpath('div[3]/a/h4/text()').extract()[0].strip()
#     item['author'] = sel.xpath('div[3]/p[1]/a/text()').extract()[0].split('\xa0')[-1]
#     item['rating'] = float(sel.xpath('div[3]/div[1]/p/span/text()').extract()[0])
#     item['tags'] = ','.join(sel.xpath('div[3]/div[2]/a/text()').extract())
#     item['category'] = sel.xpath('div[3]/div[3]/a/text()').extract()[0]
#     yield item
