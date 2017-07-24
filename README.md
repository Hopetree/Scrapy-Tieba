## 关于百度贴吧的scrapy爬虫和简单数据分析
### 一、爬虫部分
- 主爬虫项目文件为Tieba文件
- 项目结构
    - run_scrapy.py
    </br>启动项目的文件
    - Tieba\Tieba中文件为爬虫文件，包含scrapy爬虫基本的文件，不做过多介绍
- 项目配置
    - settings.py 的配置信息，见注释
```markdown
# 开启item存储
# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'Tieba.pipelines.TiebaPipeline': 300,
}
```
```markdown
# MYSQL数据库连接配置
MYSQL_HOST = "localhost"
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PW = 'python'
MYSQL_DB = 'tieba'
MYSQL_CHARSET = 'utf8mb4'
# 表格名称
MYSQL_TABLE = 'sanhe'
```
```markdown
# 爬虫开始链接和总页码数
# 格式统一为这种结构http://tieba.baidu.com/f?kw=%E9%BE%99%E5%8D%8E&ie=utf-8
BASE_URL = 'http://tieba.baidu.com/f?kw=%E9%BE%99%E5%8D%8E&ie=utf-8'
TOTAL_PAGE = 100
```
- 爬虫部分和数据保存到数据库的部分可以看具体代码及注释


### 二、数据分析部分
- 本次分析的数据是“龙华吧”前100页共91000多条数据
    </br>虽然信息是用MySQL收集的，但是由于数据量不是很大，所以数据的分析
    部分主要是用的Excel整理的，整理后的数据保存在basedata.ini中
- 数据分析的文件是analysis.py具体可视化方法见代码及注释
</br>数据的展现形式主要是图表，使用的可视化库是`pyecharts` 
- 首先来看贴吧人的等级分布吧，等级从1-15级，分析代码如下
```markdown
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
```
![1](https://github.com/Hopetree/Scrapy-Tieba/blob/master/pic/%E7%AD%89%E7%BA%A7%E5%88%86%E5%B8%83%E6%9D%A1%E5%BD%A2%E5%9B%BE.png)
