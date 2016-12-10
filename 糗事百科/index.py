# coding:utf-8

import time
import requests
from pyquery import PyQuery as pqy

class QB:

    def __init__(self):
        self.BaseUrl = "http://www.qiushibaike.com/hot/page/"
        self.Flag = True
        self.StartPage = 1
        self.EndPage = None
        self.Headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}

    #首先获取糗事百科第一页的相关数据
    def getIndexContent(self, baseUrl):
        content = requests.get(baseUrl, headers=self.Headers).content
        return content

    #打印第一页相关信息
    def printIndexInfo(self):
        content = self.getIndexContent(self.BaseUrl)
        jq = pqy(content)
        #总页数
        max_Page_num = jq(".page-numbers").eq(-1).text()
        #每页显示数
        avgCount = len(jq(".content"))
        #所有段子数量
        allJoke = int(max_Page_num) * avgCount
        #保存总页数
        self.maxPage = int(max_Page_num)
        print "相关信息如下：\n" + "当前分类下的段子总共有" + str(max_Page_num) + "页\n每页段子显示数量为" + str(avgCount) + "条\n总段子数量约为" + str(allJoke) + "条\n"
        model = int(raw_input("请选择爬取模式，\n 1、为全部爬取 \n 2、为部分爬取（部分爬取需要输入开始页码和结束页码）\n"))
        if(model == 2):
            self.StartPage = int(raw_input("请输入开始页码：\n"))
            self.EndPage = int(raw_input("请输入结束页码：\n"))
            if(self.StartPage > 0 and self.EndPage > 0):
                self.Flag = False
        self.getPageUrlByPageNum()

    #根据页码生成需要爬取的url地址
    def getPageUrlByPageNum(self):
        links = None
        if(self.Flag):
            links = [self.BaseUrl + '%d/' % i for i in range(1, self.maxPage + 1)]
        else:
            links = [self.BaseUrl + '%d/' % i for i in range(self.StartPage, self.EndPage + 1)]
        return links

    #开始爬取页面，并打印
    def printPageContent(self):
        links = self.getPageUrlByPageNum()
        for (index, i) in enumerate(links):
            #防止爬虫被屏蔽，暂停1秒
            time.sleep(1)
            content = self.getIndexContent(i)
            jq = pqy(content)
            items = jq(".content")
            if(len(items) > 0):
                print "正在爬取第" + str(index + self.StartPage) + "页，地址：" + i + "\n"
                for (num, j) in enumerate(items):
                    print u"第" + str(num + 1) + u"条：" + items(j).text() + "\n"
            else:
                print "该页暂无数据可爬取..."

    def start(self):
        self.printIndexInfo()
        self.printPageContent()
qb = QB()
qb.start()