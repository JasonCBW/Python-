# coding:utf-8

import requests
from pyquery import PyQuery as pqy

class BT:

    def __init__(self, baseUrl):
        self.baseURL = baseUrl

    def getPageContent(self):
        res = requests.get("http://www.bttiantang.com/?PageNo=2")
        jq = pqy(res.content)
        items = jq(".ml .item")
        return items

    def getUrlList(self, items):
        #去除多余的一条广告链接
        urlCount = len(items) - 1
        if (urlCount > 0):
            print "共" + str(urlCount) + "条资源" + "\n"
            for i in items:
                #根据电影名称来判断是否是广告
                items(i).find('i').empty()
                movieName = items(i).find(".tt b").text()
                if(movieName != ""):
                    link = self.baseURL + items(i).find(".tt a").attr("href")
                    print u"电影名称：" + movieName + "\t" + u"发布日期：" + items(i).find(".tt span").text() + "\t" + u"详情页面：" + link + "\n"
                    self.getDownUrl(link)
                    print "-" * 150 + "\n"
        else:
            print "该页暂无结果"

    def getDownUrl(self, url):
        res = requests.get(url)
        jq = pqy(res.content)
        downLink = jq(".tinfo a")
        downCount = len(downLink)
        print "电影下载页面:" + "\n"
        if(downCount > 0):
            print "该电影共找到" + str(downCount) + "条资源" + "\n"
            for i in downLink:
                print self.baseURL + downLink(i).attr("href")
                #p.attr(id='hello', class_='hello2')
        else:
            print "暂无该电影的下载资源,敬请期待!!!"


baseUrl = "http://www.bttiantang.com"
bt = BT(baseUrl)
bt.getUrlList(bt.getPageContent())