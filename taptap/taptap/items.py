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
    install_num = scrapy.Field()  # 安装人数
    follow_num = scrapy.Field()  # 关注人数

    def get_insert_sql(self):
        return "insert into allgame(id,name,author,rating,tags,category,install_num,follow_num) Values (%s,%s,%s,%s,%s,%s,%s,%s)"

    def get_select_sql(self):
        return "select id from allgame where id=%s"

    def get_params(self):
        return (self.get('id'), self.get('name'), self.get('author'), self.get('rating'), self.get('tags'),
                self.get('category'), self.get('install_num'), self.get('follow_num'))

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
        game['install_num'] = self.get('install_num')
        game['follow_num'] = self.get('follow_num')
        return game


# 排行榜游戏
class RatingItem(GameItem):
    top = scrapy.Field()  # 排名

    def get_params(self):
        return (
            self.get('top'), self.get('id'), self.get('name'), self.get('author'), self.get('rating'), self.get('tags'),
            self.get('category'), self.get('install_num'), self.get('follow_num'))


# 热门榜
class DownloadItem(RatingItem):
    def get_insert_sql(self):
        return "insert into download(top,id,name,author,rating,tags,category,install_num,follow_num) Values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    def get_select_sql(self):
        return "select id from download where id=%s"


# 新品榜
class NewItem(RatingItem):
    def get_insert_sql(self):
        return "insert into new(top,id,name,author,rating,tags,category,install_num,follow_num) Values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    def get_select_sql(self):
        return "select id from new where id=%s"


# 预约榜
class ReserveItem(RatingItem):
    def get_insert_sql(self):
        return "insert into reserve(top,id,name,author,rating,tags,category,install_num,follow_num) Values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    def get_select_sql(self):
        return "select id from reserve where id=%s"


# 热卖榜
class SellItem(RatingItem):
    def get_insert_sql(self):
        return "insert into sell(top,id,name,author,rating,tags,category,install_num,follow_num) Values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    def get_select_sql(self):
        return "select id from sell where id=%s"


# 热玩榜
class PlayedItem(RatingItem):
    def get_insert_sql(self):
        return "insert into played(top,id,name,author,rating,tags,category,install_num,follow_num) Values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    def get_select_sql(self):
        return "select id from played where id=%s"


# 安利墙
class AmwayItem(GameItem):
    def get_insert_sql(self):
        return "insert into amway(id,name,author,rating,tags,category,install_num,follow_num) Values (%s,%s,%s,%s,%s,%s,%s,%s)"

    def get_select_sql(self):
        return "select id from amway where id=%s"


# 往期推荐
class RecommendItem(GameItem):
    def get_insert_sql(self):
        return "insert into recommend(id,name,author,rating,tags,category,install_num,follow_num) Values (%s,%s,%s,%s,%s,%s,%s,%s)"

    def get_select_sql(self):
        return "select id from recommend where id=%s"


# taptap独家
class SoleItem(GameItem):
    def get_insert_sql(self):
        return "insert into sole(id,name,author,rating,tags,category,install_num,follow_num) Values (%s,%s,%s,%s,%s,%s,%s,%s)"

    def get_select_sql(self):
        return "select id from sole where id=%s"


# 单机游戏
class AloneItem(GameItem):
    def get_insert_sql(self):
        return "insert into alone(id,name,author,rating,tags,category,install_num,follow_num) Values (%s,%s,%s,%s,%s,%s,%s,%s)"

    def get_select_sql(self):
        return "select id from alone where id=%s"


# 角色扮演游戏
class RpgItem(GameItem):
    def get_insert_sql(self):
        return "insert into rpg(id,name,author,rating,tags,category,install_num,follow_num) Values (%s,%s,%s,%s,%s,%s,%s,%s)"

    def get_select_sql(self):
        return "select id from rpg where id=%s"


# 动作游戏
class ActionItem(GameItem):
    def get_insert_sql(self):
        return "insert into action(id,name,author,rating,tags,category,install_num,follow_num) Values (%s,%s,%s,%s,%s,%s,%s,%s)"

    def get_select_sql(self):
        return "select id from action where id=%s"


# MOBA游戏
class MobaItem(GameItem):
    def get_insert_sql(self):
        return "insert into moba(id,name,author,rating,tags,category,install_num,follow_num) Values (%s,%s,%s,%s,%s,%s,%s,%s)"

    def get_select_sql(self):
        return "select id from moba where id=%s"


# 策略游戏
class StrategyItem(GameItem):
    def get_insert_sql(self):
        return "insert into strategy(id,name,author,rating,tags,category,install_num,follow_num) Values (%s,%s,%s,%s,%s,%s,%s,%s)"

    def get_select_sql(self):
        return "select id from strategy where id=%s"


# 卡牌游戏
class CardItem(GameItem):
    def get_insert_sql(self):
        return "insert into card(id,name,author,rating,tags,category,install_num,follow_num) Values (%s,%s,%s,%s,%s,%s,%s,%s)"

    def get_select_sql(self):
        return "select id from card where id=%s"


# 生存游戏
class SurvivalItem(GameItem):
    def get_insert_sql(self):
        return "insert into survival(id,name,author,rating,tags,category,install_num,follow_num) Values (%s,%s,%s,%s,%s,%s,%s,%s)"

    def get_select_sql(self):
        return "select id from survival where id=%s"


# 模拟游戏
class SimulationItem(GameItem):
    def get_insert_sql(self):
        return "insert into simulation(id,name,author,rating,tags,category,install_num,follow_num) Values (%s,%s,%s,%s,%s,%s,%s,%s)"

    def get_select_sql(self):
        return "select id from simulation where id=%s"


# 竞速游戏
class RacingItem(GameItem):
    def get_insert_sql(self):
        return "insert into racing(id,name,author,rating,tags,category,install_num,follow_num) Values (%s,%s,%s,%s,%s,%s,%s,%s)"

    def get_select_sql(self):
        return "select id from racing where id=%s"


# 益智游戏
class PuzzleItem(GameItem):
    def get_insert_sql(self):
        return "insert into puzzle(id,name,author,rating,tags,category,install_num,follow_num) Values (%s,%s,%s,%s,%s,%s,%s,%s)"

    def get_select_sql(self):
        return "select id from puzzle where id=%s"


# 二次元游戏
class QuadraticItem(GameItem):
    def get_insert_sql(self):
        return "insert into quadratic(id,name,author,rating,tags,category,install_num,follow_num) Values (%s,%s,%s,%s,%s,%s,%s,%s)"

    def get_select_sql(self):
        return "select id from quadratic where id=%s"
