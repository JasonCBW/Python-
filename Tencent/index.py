# coding:utf-8

import requests
import urllib2
from pyquery import PyQuery as pqy
from Tencent.items import *

class TencentSpider:

    def __init__(self):
        self.baseUrl = "http://hr.tencent.com/position.php?&start=20#a"

    def parse_item(self):
        source = urllib2.urlopen(self.baseUrl)
        jq = pqy(source.read())
        sites = jq(".tablelist tr")
        sites.remove('.h')
        sites('.h').empty()
        sites('.f').empty()
        print "职位名称\t\t\t" + "职位类别\t" + "人数\t" + "地点\t" + "发布日期\t"
        for s in sites:
            print sites(s).find('a').text() + "\t" + sites(s).find('td').eq(1).text() + "\t\t" + sites(s).find('td').eq(2).text() + sites(s).find('td').eq(3).text() + \
                  sites(s).find('td').eq(4).text()

tt = TencentSpider()
tt.parse_item()