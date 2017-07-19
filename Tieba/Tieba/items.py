# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TiebaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 帖子标题1
    tie_title = scrapy.Field()
    # 跟帖总数2
    tie_num = scrapy.Field()
    # 跟帖楼层3
    post_no = scrapy.Field()
    # 层主昵称4
    user_name = scrapy.Field()
    # 层主ID5
    user_id = scrapy.Field()
    # 层主性别6
    user_sex = scrapy.Field()
    # 层主等级7
    level_id = scrapy.Field()
    # 层主头衔8
    level_name = scrapy.Field()
    # 层主经验值9
    cur_score = scrapy.Field()
    # 层主主页10
    user_zone = scrapy.Field()
    # 层主头像11
    user_photo = scrapy.Field()
    # 发帖来源12
    user_from = scrapy.Field()
    # 跟帖时间13
    create_date = scrapy.Field()
    # 回复数量14
    comment_num = scrapy.Field()
    # 是否吧务15
    is_bawu = scrapy.Field()
    # 帖子链接
    tie_link = scrapy.Field()







