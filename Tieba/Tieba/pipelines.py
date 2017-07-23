# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.conf import settings
import pymysql

class TiebaPipeline(object):
    def __init__(self):
        # 数据库信息从配置读取
        self.table = settings['MYSQL_TABLE']
        self.conn = pymysql.Connect(
            host=settings['MYSQL_HOST'],
            port=settings['MYSQL_PORT'],
            user=settings['MYSQL_USER'],
            password=settings['MYSQL_PW'],
            db=settings['MYSQL_DB'],
            charset=settings['MYSQL_CHARSET']
        )
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        # 表格从配置中读取
        sql = '''INSERT INTO `{}`(tie_title,tie_num,post_no,user_name,user_id,user_sex,level_id,level_name,cur_score,user_zone,
        user_photo,user_from,create_date,comment_num,is_bawu,tie_link) VALUES ("{}","{}","{}","{}","{}","{}","{}","{}",
        "{}","{}","{}","{}","{}","{}","{}","{}")'''
        try:
            self.cursor.execute(sql.format(self.table,item['tie_title'],item['tie_num'],item['post_no'],item['user_name'],
                                item['user_id'],item['user_sex'],item['level_id'],item['level_name'],item['cur_score'],item['user_zone'],
                                item['user_photo'],item['user_from'],item['create_date'],item['comment_num'],
                                item['is_bawu'],item['tie_link']))
            self.conn.commit()
        except Exception as e:
            print("保存信息失败，原因是{}".format(e))
            self.conn.rollback()

        return item
