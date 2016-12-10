# coding:utf-8

import time
from pyquery import PyQuery as pqy
from selenium import webdriver


class TBook:

    def __init__(self):
        self.baseURL = "http://www.tiantianbook.cn"
        self.headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}

    #获取荐购榜和畅销榜
    def getPageContent(self):
        driver = webdriver.PhantomJS()
        driver.get(self.baseURL)
        # 暂停一秒（目前只知道暂停一秒后能正常获取数据）
        time.sleep(2)
        jq = pqy(driver.page_source)
        #得到荐购榜和畅销榜
        content = jq(".h_rank_container ul")
        return content
        driver.close()

    #打印荐购榜和畅销榜信息
    def printBookList(self):
        content = self.getPageContent()
        for (index, ul) in enumerate(content):
            if(index == 0):
                print "荐购榜："
            else:
                print "畅销榜："
            ulContent = content(ul).children("li")
            for (li, item) in enumerate(ulContent):
                print str(li + 1) + u"、" + ulContent(item).find("a").attr("title") + " " * 5 + u"链接地址：" + \
                      self.baseURL + ulContent(item).find("a").attr("href")
            print "\n"


tb = TBook()
tb.printBookList()