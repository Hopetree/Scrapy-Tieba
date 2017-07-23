# -*- coding: utf-8 -*-

# 导入配置信息
from scrapy.conf import settings
from Tieba.items import TiebaItem
import scrapy
import re

class tieba_spider(scrapy.Spider):
    name = "Tieba"
    allowed_domains = ['tieba.baidu.com']
    # 起始链接从配置读取
    start_urls = [settings['BASE_URL']]

    def parse(self, response):
        base_url = '{}&pn={}'
        # 总页码数从配置获取
        pagenum = settings['TOTAL_PAGE']
        for page in range(pagenum):
            the_url = base_url.format(settings['BASE_URL'],page * 50)
            yield scrapy.Request(the_url, callback=self.parse_get_urls)

    # 获取一页的所有帖子
    def parse_get_urls(self, response):
        endurls = re.findall('<a href="(/p/.*?)" title=',response.text)
        for each in endurls:
            tz_url = "http://tieba.baidu.com{}".format(each)
            yield scrapy.Request(url=tz_url,callback=self.parse_get_infos)

    # 获取一个帖子的所有回帖，需要递归翻页
    def parse_get_infos(self,response):
        # 获取请求的URL，添加到ITEM中
        req_url = response.url
        # 提取标题和回帖数
        title = response.xpath('//*[@id="j_core_title_wrap"]/div[2]/h1/@title').extract_first()
        num = response.xpath('//*[@id="thread_theme_7"]/div[1]/ul/li[2]/span[1]/text()').extract_first()
        '''替换提取的信息中的参数，避免使用eval报错'''
        null,false,true,none = "","","",""
        tiezis = response.xpath('//*[@id="j_p_postlist"]/div/@data-field')
        for each in tiezis:
            item = TiebaItem()
            info = eval(each.extract())
            item['tie_title'] = title
            item['tie_num'] = num
            item['post_no'] = info['content']['post_no']
            item['user_name'] = info['author']['user_name']
            item['user_id'] = info['author']['user_id']
            item['user_sex'] = info['author']['user_sex']
            item['level_id'] = info['author']['level_id']
            item['level_name'] = info['author']['level_name']
            item['cur_score'] = info['author']['cur_score']
            item['user_zone'] = info['author']['name_u']
            item['user_photo'] = info['author']['portrait']
            item['user_from'] = info['content']['open_type']
            item['create_date'] = info['content']['date']
            item['comment_num'] = info['content']['comment_num']
            item['is_bawu'] = info['author']['bawu']
            item['tie_link'] = req_url
            yield item
        # 判断是否有下一页，如果有就递归翻页爬完所有回帖
        try:
            next_text = response.xpath('//*[@id="thread_theme_7"]/div[1]/ul/li[1]/a/text()').extract()[-2]
            # 这个可以判断是否有下一页
            if next_text == "下一页":
                next_url = response.xpath('//*[@id="thread_theme_7"]/div[1]/ul/li[1]/a/@href').extract()[-2]
                # 下一页的链接
                next_url = "http://tieba.baidu.com"+next_url
                yield scrapy.Request(next_url,self.parse_get_infos)
        except:
            pass
