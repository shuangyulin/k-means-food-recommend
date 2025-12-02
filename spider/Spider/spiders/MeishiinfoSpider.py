# # -*- coding: utf-8 -*-

# 数据爬取文件

import scrapy
import pymysql
import pymssql
from ..items import MeishiinfoItem
import time
from datetime import datetime,timedelta
import datetime as formattime
import re
import random
import platform
import json
import os
import urllib
from urllib.parse import urlparse
import requests
import emoji
import numpy as np
from DrissionPage import Chromium
import pandas as pd
from sqlalchemy import create_engine
from selenium.webdriver import ChromeOptions, ActionChains
from scrapy.http import TextResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import pandas as pd
from sqlalchemy import create_engine
from selenium.webdriver import ChromeOptions, ActionChains
from scrapy.http import TextResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
# 美食信息
class MeishiinfoSpider(scrapy.Spider):
    name = 'meishiinfoSpider'
    custom_settings = {
        'HTTPERROR_ALLOWED_CODES': [400,403],
        'RETRY_HTTP_CODES': [500, 503]
    }
    spiderUrl = 'https://waimai-guide.ele.me/h5/mtop.relationrecommend.elemetinyapprecommend.recommend/1.0/5.0/?jsv=2.7.2&appKey=12574478&t=1744690679113&sign=21232821f9d34848a1116b007840c1d9&api=mtop.relationrecommend.ElemeTinyAppRecommend.recommend&v=1.0&type=originaljson&dataType=json&timeout=10000&mainDomain=ele.me&subDomain=waimai-guide&H5Request=true&ttid=h5%40chrome_android_135.0.0.0&SV=5.0&pageDomain=ele.me&data=%7B%22appId%22%3A%2226551%22%2C%22type%22%3A%22originaljson%22%2C%22params%22%3A%22%7B%5C%22appId%5C%22%3A%5C%2226551%5C%22%2C%5C%22_input_charset%5C%22%3A%5C%22UTF-8%5C%22%2C%5C%22_output_charset%5C%22%3A%5C%22UTF-8%5C%22%2C%5C%22gatewayApiType%5C%22%3A%5C%22mtop%5C%22%2C%5C%22x-ele-scene%5C%22%3A%5C%22search%5C%22%2C%5C%22mtop_api_version%5C%22%3A%5C%221.0%5C%22%2C%5C%22channelCode%5C%22%3A%5C%220%5C%22%2C%5C%22platform%5C%22%3A%5C%22999%5C%22%2C%5C%22alipayChannel%5C%22%3A1%2C%5C%22sversion%5C%22%3A%5C%225.3%5C%22%2C%5C%22offset%5C%22%3A10%2C%5C%22limit%5C%22%3A5%2C%5C%22n%5C%22%3A5%2C%5C%22page%5C%22%3A3%2C%5C%22latitude%5C%22%3A%5C%2236.819372%5C%22%2C%5C%22longitude%5C%22%3A%5C%22118.028709%5C%22%2C%5C%22keyword%5C%22%3A%5C%22%E7%BE%8E%E9%A3%9F%5C%22%2C%5C%22rankId%5C%22%3A%5C%22382025cdeda3414e91ec00a18436e143%5C%22%2C%5C%22searchExtraParams%5C%22%3A%5C%22null%5C%22%2C%5C%22searchMode%5C%22%3A2%2C%5C%22fixSearch%5C%22%3A%5C%220%5C%22%2C%5C%22storeParams%5C%22%3A%5C%22%7B%7D%5C%22%7D%22%7D&bx_et=fqRmTuiSPKWj1f4tmQfjKwTyCGD8Ho11fhFOX1IZUgSWX-8ZlVVGq3vA0EpvIfYwxq_tcCKlQHL_H1I9sLNMRFOxl13fGE11_DnK9hYXl19Z9aNm2UuN58vlvIcplE11Qima9XEM38UIoG-N3g8P-gyV_OSNz4bNWoyagh8rrNsz_ZWVQTzPRZrVbjknHi9wCQo52bbRoEzpMZXcjWS3s50OotjeugmEWQc5nM8Vq5oI7lQGjgOE2YYWxK-APhcnq6JBqCXFsjqCoL8haiCEK8fDynOhgBm0MaCRD9JNEql2rsjcQZ6n6m1DQnOGhK4sRU52VpsC3Yi5rIddIM6u4m8JriWHInn7_ipHz3XpwuFdTptks95F4RwzLtQz1Mhk5Rw13a_lASq2ZaE1B0iqr42E-t75z23orRw13a_lv40uL2XVPaud.'
    start_urls = spiderUrl.split(";")
    protocol = ''
    hostname = ''
    realtime = False


    def __init__(self,realtime=False,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.realtime = realtime=='true'

    def start_requests(self):

        plat = platform.system().lower()
        if not self.realtime and (plat == 'linux' or plat == 'windows'):
            connect = self.db_connect()
            cursor = connect.cursor()
            if self.table_exists(cursor, 'fg054mx8_meishiinfo') == 1:
                cursor.close()
                connect.close()
                self.temp_data()
                return
        pageNum = 1 + 1

        for url in self.start_urls:
            if '{}' in url:
                for page in range(1, pageNum):

                    next_link = url.format(page)
                    yield scrapy.Request(
                        url=next_link,
                        callback=self.parse
                    )
            else:
                yield scrapy.Request(
                    url=url,
                    callback=self.parse
                )

    # 列表解析
    def parse(self, response):
        _url = urlparse(self.spiderUrl)
        self.protocol = _url.scheme
        self.hostname = _url.netloc
        plat = platform.system().lower()
        if not self.realtime and (plat == 'linux' or plat == 'windows'):
            connect = self.db_connect()
            cursor = connect.cursor()
            if self.table_exists(cursor, 'fg054mx8_meishiinfo') == 1:
                cursor.close()
                connect.close()
                self.temp_data()
                return
        data = json.loads(response.body)
        try:
            list = data["data"]["result"][0]["listItems"]
        except:
            pass
        for item in list:
            fields = MeishiinfoItem()


            try:
                fields["shopname"] = emoji.demojize(self.remove_html(str( item["info"]["restaurant"]["name"] )))

            except:
                pass
            try:
                fields["score"] = float( item["info"]["restaurant"]["rating"])
            except:
                pass
            try:
                fields["qsprice"] = float( item["info"]["restaurant"]["piecewiseAgentFee"]["rules"][0]["price"])
            except:
                pass
            try:
                fields["psprice"] = float( item["info"]["restaurant"]["piecewiseAgentFee"]["rules"][0]["fee"])
            except:
                pass
            try:
                fields["msname"] = emoji.demojize(self.remove_html(str( item["name"] )))

            except:
                pass
            try:
                fields["imgurl"] = emoji.demojize(self.remove_html(str( item["imagePath"] )))

            except:
                pass
            try:
                fields["monthsales"] = int( item["monthSales"])
            except:
                pass
            try:
                fields["jiage"] = float( item["price"])
            except:
                pass
            try:
                fields["stock"] = int( item["stock"])
            except:
                pass
            try:
                fields["shopurl"] = emoji.demojize(self.remove_html(str( item["info"]["restaurant"]["scheme"] )))

            except:
                pass
            yield fields

    # 详情解析
    def detail_parse(self, response):
        fields = response.meta['fields']
        return fields

    # 数据清洗
    def pandas_filter(self):
        engine = create_engine('mysql+pymysql://root:123456@localhost/spiderfg054mx8?charset=UTF8MB4')
        df = pd.read_sql('select * from meishiinfo limit 50', con = engine)

        # 重复数据过滤
        df.duplicated()
        df.drop_duplicates()

        #空数据过滤
        df.isnull()
        df.dropna()

        # 填充空数据
        df.fillna(value = '暂无')

        # 异常值过滤

        # 滤出 大于800 和 小于 100 的
        a = np.random.randint(0, 1000, size = 200)
        cond = (a<=800) & (a>=100)
        a[cond]

        # 过滤正态分布的异常值
        b = np.random.randn(100000)
        # 3σ过滤异常值，σ即是标准差
        cond = np.abs(b) > 3 * 1
        b[cond]

        # 正态分布数据
        df2 = pd.DataFrame(data = np.random.randn(10000,3))
        # 3σ过滤异常值，σ即是标准差
        cond = (df2 > 3*df2.std()).any(axis = 1)
        # 不满⾜条件的⾏索引
        index = df2[cond].index
        # 根据⾏索引，进⾏数据删除
        df2.drop(labels=index,axis = 0)

    # 去除多余html标签
    def remove_html(self, html):
        if html == None:
            return ''
        pattern = re.compile(r'<[^>]+>', re.S)
        return pattern.sub('', html).strip()

    # 数据库连接
    def db_connect(self):
        type = self.settings.get('TYPE', 'mysql')
        host = self.settings.get('HOST', 'localhost')
        port = int(self.settings.get('PORT', 3306))
        user = self.settings.get('USER', 'root')
        password = self.settings.get('PASSWORD', '123456')

        try:
            database = self.databaseName
        except:
            database = self.settings.get('DATABASE', '')

        if type == 'mysql':
            connect = pymysql.connect(host=host, port=port, db=database, user=user, passwd=password, charset='utf8mb4')
        else:
            connect = pymssql.connect(host=host, user=user, password=password, database=database)
        return connect

    # 断表是否存在
    def table_exists(self, cursor, table_name):
        cursor.execute("show tables;")
        tables = [cursor.fetchall()]
        table_list = re.findall('(\'.*?\')',str(tables))
        table_list = [re.sub("'",'',each) for each in table_list]

        if table_name in table_list:
            return 1
        else:
            return 0

    # 数据缓存源
    def temp_data(self):

        connect = self.db_connect()
        cursor = connect.cursor()
        sql = '''
            insert into `meishiinfo`(
                id
                ,shopname
                ,score
                ,qsprice
                ,psprice
                ,msname
                ,imgurl
                ,monthsales
                ,jiage
                ,stock
                ,shopurl
            )
            select
                id
                ,shopname
                ,score
                ,qsprice
                ,psprice
                ,msname
                ,imgurl
                ,monthsales
                ,jiage
                ,stock
                ,shopurl
            from `fg054mx8_meishiinfo`
            where(not exists (select
                id
                ,shopname
                ,score
                ,qsprice
                ,psprice
                ,msname
                ,imgurl
                ,monthsales
                ,jiage
                ,stock
                ,shopurl
            from `meishiinfo` where
                `meishiinfo`.id=`fg054mx8_meishiinfo`.id
            ))
            order by rand()
            limit 50;
        '''

        cursor.execute(sql)
        connect.commit()
        connect.close()
