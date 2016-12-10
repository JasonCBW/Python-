# coding:utf-8

import requests
from pyquery import PyQuery as pqy

class DYTT:

    def __init__(self, baseUrl):
        self.baseURL = baseUrl

    #获取页面内容
    def getPageContent(self):
        req = requests.get(self.baseURL)
        jq = pqy(req.content)
        #指定的板块内容(eq(0)是指本人只关注本年度的新片,其他版块不需要显示,需要显示全部版块择去掉eq(0))
        contents = jq(".co_area2").eq(0)
        return contents

    #打印各个板块的资源
    def printPageContent(self):
        content = pqy(self.getPageContent())
        for v in content:
            #所有资源对象
            ulContent = content(v).find(".co_content222 li")
            print u"板块名称:" + content(v).find(".title_all span").text()
            print u"板块资源:"
            for index, item in enumerate(ulContent):
                url = self.baseURL + ulContent(item).find("a").attr("href")
                print str(index + 1) + u"、电影名称：" + ulContent(item).find("a").attr("title") + "\t" + u"详情页面：" \
                + url
                self.getDownLinks(url)

    #获取详情页面的下载链接
    def getDownLinks(self, url):
        try:
            res = requests.get(url).content
            jq = pqy(res)
            #获取到迅雷下载链接
            links = jq("#Zoom table a")
            print "迅雷链接地址:"
            if(len(links) > 0):
                for k, v in enumerate(links):
                    print str(k + 1) + ".\t" + links(v).attr("href")
            else:
                print "该影片暂无资源或因网络原因未获取到下载链接,请点击详情页面进行查看..."
            print "*" * 150 + "\n"
        except Exception, e:
            if(hasattr(e, "reason")):
                print e.reason

baseUrl = "http://www.dy2018.com"
dytt = DYTT(baseUrl)
dytt.printPageContent()