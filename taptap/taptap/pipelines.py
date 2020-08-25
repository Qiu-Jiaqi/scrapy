# -*- coding: utf-8 -*-


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymysql
import copy
from twisted.enterprise import adbapi


class TaptapPipeline(object):
    def __init__(self, db_pool):
        self.db_pool = db_pool

    # 函数名固定，会被scrapy调用，直接可用settings的值
    @classmethod
    def from_settings(cls, settings):
        db_params = dict(
            host=settings['MYSQL_HOST'],
            user=settings['MYSQL_USER'],
            password=settings['MYSQL_PASSWORD'],
            port=settings['MYSQL_PORT'],
            database=settings['MYSQL_DBNAME'],
            charset=settings['MYSQL_CHARSET'],
            use_unicode=True,
            cursorclass=pymysql.cursors.DictCursor  # 指定cursor类型
        )
        # 连接数据池ConnectionPool
        db_pool = adbapi.ConnectionPool('pymysql', **db_params)
        # 返回实例化参数
        return cls(db_pool)

    def process_item(self, item, spider):
        # 使用twisted将MySQL插入变成异步执行。通过连接池执行具体的sql操作，返回一个对象
        # 指定操作方法和操作数据
        asynItem = copy.deepcopy(item)
        query = self.db_pool.runInteraction(self.do_insert, asynItem)
        # 添加异常处理
        query.addErrback(self.handle_error)

    # 对数据库进行插入操作，并不需要commit，twisted会自动commit
    def do_insert(self, cursor, item):
        flag = cursor.execute(item.get_select_sql(), item.get_primary())
        if flag:
            pass
        else:
            cursor.execute(item.get_insert_sql(), item.get_params())

        # 插入allgame表
        gameItem = item.get_game()
        flag = cursor.execute(gameItem.get_select_sql(), gameItem.get_primary())
        if flag:
            pass
        else:
            cursor.execute(gameItem.get_insert_sql(), gameItem.get_params())

    def handle_error(self, error):
        if error:
            print("error:", error)
