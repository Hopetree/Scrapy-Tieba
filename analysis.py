# -*- conding:utf-8 -*-

from configparser import ConfigParser
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
from scipy.misc import imread


class TEST(object):
    def __init__(self):
        cf = ConfigParser()
        cf.read('basedata.ini',encoding='utf-8')
        self.ftitle = '数据来源：“龙华吧”91521条数据'

        self.bardata = cf.items('bardata')
        self.piedata = cf.items('piedata')
        self.sexpiedata = cf.items('sexpiedata')
        self.wordcloud = cf.items('wordcloud')
        self.linedata = cf.items('linedata')
        self.fromdata = cf.items('fromdata')

    def bartest(self):
        from pyecharts import Bar
        bar = Bar('等级分布条形图',self.ftitle)
        # 利用自带的解析方法把列表解析成2个关联列表
        key,value = bar.cast(self.bardata)
        # is_datazoom_show = 参数是用来显示下滑筛选块的，默认假
        # is_label_show = 参数用来显示数值，默认假
        bar.add('等级分布',key,value,is_datazoom_show=False,is_label_show=True)
        # bar.show_config()
        bar.render(r"pic\等级分布条形图.html")
        print('成功输出Bar测试网页')

    def pietest(self):
        from pyecharts import Pie
        pie = Pie('头衔分布饼形图',self.ftitle,height=600,title_pos='left')
        key,value = pie.cast(self.piedata)
        pie.add('人数',key,value,is_label_show=True,is_legend_show=False,radius=[30,70])
        pie.render(r'pic\头衔分布饼形图.html')
        print('饼形图输出Pie测试网页')

    def sexpietest(self):
        from pyecharts import Pie
        pie = Pie('性别分布饼形图',self.ftitle,height=500)
        key,value = pie.cast(self.sexpiedata)
        pie.add('人数',key,value,is_label_show=True,center=[50,55],rosetype='area')
        pie.render(r'pic\性别分布饼形图.html')
        print('性别饼形图输出成功')

    def wordcloudtest(self):
        from pyecharts import WordCloud
        import random
        wd = WordCloud('回帖数词云图')
        key,value = wd.cast(self.wordcloud)
        shapes = ['circle', 'cardioid', 'diamond', 'triangle-forward', 'triangle', 'pentagon', 'star']
        wd.add('',key,value,shape=shapes[0])
        wd.render(r'pic\主要发帖人词云图.html')
        print('词云图测试成功')

    def linetest(self):
        from pyecharts import Line
        line = Line('发帖时间分布折线图',self.ftitle)
        key,value = line.cast(self.linedata)
        line.add('发帖人数',key,value,is_label_show=True,is_fill=True,area_opacity=0.3,is_smooth=True)
        line.render(r'pic\发帖时间折线图.html')
        print("折线图测试成功输出")

    def fromtest(self):
        from pyecharts import Pie
        pie = Pie('帖子来源饼形图',self.ftitle,title_pos='center')
        key,value = pie.cast(self.fromdata)
        pie.add('帖子数',key,value,is_label_show=True,radius=[35,65],center=[50,55],legend_pos='left',legend_orient='vertical')
        pie.render(r'pic\帖子来源饼形图.html')

    def wordcloud_1(self,imagename,cloudname,fontname):
        wordlist = self.wordcloud
        coloring = imread(imagename)
        # 词云图的最大尺寸取决于比较图
        wc = WordCloud(background_color='white',mask=coloring,stopwords=STOPWORDS,font_path=fontname,max_font_size=150,
                       height=800,width=600)
        # 参数是一个字典
        wc.generate_from_frequencies({i:int(dict(wordlist)[i]) for i in dict(wordlist)})
        plt.imshow(wc)
        plt.axis('off')
        plt.figure()
        wc.to_file(cloudname)
        print("词云图生成完毕")

if __name__ == '__main__':
    test = TEST()
    test.bartest()
    test.pietest()
    test.sexpietest()
    test.wordcloudtest()
    test.linetest()
    test.fromtest()
    test.wordcloud_1(r"pic\logo.jpg",r"pic\wordcloud.png",r"pic\兰亭黑简.TTF")