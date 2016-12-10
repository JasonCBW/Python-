# coding:utf-8

import urllib2
import re
import time
import types
import page
import mysql
import sys
from bs4 import BeautifulSoup

class Spider:

    #初始化
    def __init__(self):
        self.page_num = 1
        self.total_num = None
        self.page_spider = page.Page()
        self.mysql = mysql.MySql()

    def getPageContent(self, url):
        req = urllib2.Request(url)
        res = urllib2.urlopen(req)
        content = res.read()
        return content

    def getItemList(self, pageContent):
        #http://iask.sina.com.cn/b/3KIEPjgv9Z.html
        pattern = re.compile('<div class="question-title".*?<a href="(.*?)".*?>(.*?)</a>', re.S)
        items = re.findall(pattern, pageContent)
        for item in items:
            print "在线问答地址：" + "http://iask.sina.com.cn" + item[0] + "\t" + "题目标题：" + str(item[1])

    def start(self):
        content = self.getPageContent(self.baseURL);
        self.getItemList(content)

baseUrl = "http://iask.sina.com.cn/c/1090.html"
s = Spider(baseUrl)
s.start()