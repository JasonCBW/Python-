# coding:utf-8

import requests
from pyquery import PyQuery as pqy


class CSDN:

    def __init__(self):
        self.baseURL = "http://blog.csdn.net/pleasecallmewhy/article/details/8922826"
        self.headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}

    def getContent(self):
        content = requests.get(self.baseURL, headers=self.headers).content
        jq = pqy(content).find("#blog_rank")
        jq("li").eq(2).empty()
        print jq.text()

csdn = CSDN()
csdn.getContent()
