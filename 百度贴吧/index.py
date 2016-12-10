# coding:utf-8

from pyquery import PyQuery as pyq

class TieBa:

    def __init__(self, baseUrl):
        self.baseURL = baseUrl

    def getPageContent(self):
        url = self.baseURL + "/f?kw=%E6%9D%83%E5%8A%9B%E7%9A%84%E6%B8%B8%E6%88%8F&ie=utf-8&pn=0"
        jq = pyq(url=url)
        # 所有帖子的html架构
        generalLi = jq(".j_thread_list")
        return generalLi

    def printList(self, jq):
        # 总共的帖子数
        liCount = len(jq)
        # 置顶帖子数
        topLi = 0
        # 一般帖子数
        genLi = 0
        print u"帖子种类" + "*" * 12 + u"帖子名称" + "*" * 70 + u"帖子链接" + "\n"
        for a in jq:
            if jq(a).not_('.thread_top'):
                genLi += 1
                li = jq(a)
                print " " * 3 + u"一般" + " " * 12 + li('.threadlist_title > a').attr('title') + " " * 33 + self.baseURL + li('.threadlist_title > a').attr('href')
            else:
                topLi += 1
                li = jq(a)
                print " " * 3 + u"置顶" + " " * 12 + li('.threadlist_title > a').attr('title') + " " * 33 + self.baseURL + li('.threadlist_title > a').attr('href')
        print u"该页一共有帖子" + str(liCount) + u"条，其中置顶帖子共" + str(topLi) + u"条，一般性帖子共" + str(genLi) + u"条"

baseUrl = "http://tieba.baidu.com"
tieba = TieBa(baseUrl)
tieba.printList(tieba.getPageContent())
