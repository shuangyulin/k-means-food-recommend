# 数据容器文件

import scrapy

class SpiderItem(scrapy.Item):
    pass

class MeishiinfoItem(scrapy.Item):
    # 店名
    shopname = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 起送
    qsprice = scrapy.Field()
    # 配送
    psprice = scrapy.Field()
    # 美食名称
    msname = scrapy.Field()
    # 图片
    imgurl = scrapy.Field()
    # 月销量
    monthsales = scrapy.Field()
    # 价格
    jiage = scrapy.Field()
    # 库存
    stock = scrapy.Field()
    # 商店地址
    shopurl = scrapy.Field()

