# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# 游戏
class GameItem(scrapy.Item):
    id = scrapy.Field()  # id
    name = scrapy.Field()  # 名称
    author = scrapy.Field()  # 厂商
    rating = scrapy.Field()  # 评分
    tags = scrapy.Field()  # 标签
    category = scrapy.Field()  # 分类

    def get_insert_sql(self):
        return "insert into allgame(id,name,author,rating,tags,category) Values (%s,%s,%s,%s,%s,%s)"

    def get_select_sql(self):
        return "select id from allgame where id=%s"

    def get_params(self):
        return (self.get('id'), self.get('name'), self.get('author'), self.get('rating'), self.get('tags'),
                self.get('category'))

    def get_primary(self):
        return self.get('id')

    def get_game(self):
        game = GameItem()
        game['id'] = self.get('id')
        game['name'] = self.get('name')
        game['author'] = self.get('author')
        game['rating'] = self.get('rating')
        game['tags'] = self.get('tags')
        game['category'] = self.get('category')
        return game


# 排行榜游戏
class RatingItem(GameItem):
    top = scrapy.Field()  # 排名

    def get_params(self):
        return (
            self.get('top'), self.get('id'), self.get('name'), self.get('author'), self.get('rating'), self.get('tags'),
            self.get('category'))

    def get_primary(self):
        return self.get('top')


# 热门榜
class DownloadItem(RatingItem):
    def get_insert_sql(self):
        return "insert into download(top,id,name,author,rating,tags,category) Values (%s,%s,%s,%s,%s,%s,%s)"

    def get_select_sql(self):
        return "select top from download where top=%s"


# 新品榜
class NewItem(RatingItem):
    def get_insert_sql(self):
        return "insert into new(top,id,name,author,rating,tags,category) Values (%s,%s,%s,%s,%s,%s,%s)"

    def get_select_sql(self):
        return "select top from new where top=%s"


# 预约榜
class ReserveItem(RatingItem):
    def get_insert_sql(self):
        return "insert into reserve(top,id,name,author,rating,tags,category) Values (%s,%s,%s,%s,%s,%s,%s)"

    def get_select_sql(self):
        return "select top from reserve where top=%s"


# 热卖榜
class SellItem(RatingItem):
    def get_insert_sql(self):
        return "insert into sell(top,id,name,author,rating,tags,category) Values (%s,%s,%s,%s,%s,%s,%s)"

    def get_select_sql(self):
        return "select top from sell where top=%s"


# 热玩榜
class PlayedItem(RatingItem):
    def get_insert_sql(self):
        return "insert into played(top,id,name,author,rating,tags,category) Values (%s,%s,%s,%s,%s,%s,%s)"

    def get_select_sql(self):
        return "select top from played where top=%s"


# 往期推荐
class RecommendItem(GameItem):
    def get_insert_sql(self):
        return "insert into recommend(id,name,author,rating,tags,category) Values (%s,%s,%s,%s,%s,%s)"

    def get_select_sql(self):
        return "select id from recommend where id=%s"


# taptap独家
class SoleItem(GameItem):
    def get_insert_sql(self):
        return "insert into sole(id,name,author,rating,tags,category) Values (%s,%s,%s,%s,%s,%s)"

    def get_select_sql(self):
        return "select id from sole where id=%s"
