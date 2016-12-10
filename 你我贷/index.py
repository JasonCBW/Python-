# coding:utf-8

from pyquery import PyQuery as pqy
from selenium import webdriver

class NWD:
    def __init__(self):
        self.BaseUrl = "https://member.niwodai.com/financial/financialDetail.do?fp_id=ADZUNlYwVTkFY1RgUDFeagoxVW0CaAJnBT8FMgBlU2I=&nwd=1"
        self.AjaxUrl = "https://member.niwodai.com/financial/ajax/cameraDetailPage.do?fp_id=ADZUNlYwVTkFY1RgUDFeagoxVW0CaAJnBT8FMgBlU2Y=&totalCount=98&pageNo="

    def printPage(self):
        driver = webdriver.PhantomJS()
        driver.get(self.BaseUrl)
        jq = pqy(driver.page_source)
        #得到总的页码数
        pageCount = int(jq("#loanDetail .pageout a").eq(-2).text())
        #生成待访问的ajax请求链接
        ajaxLinks = [self.AjaxUrl + str(i) for i in range(1, pageCount + 1)]
        for index, u in enumerate(ajaxLinks):
            driver.get(u)
            q = pqy(driver.page_source).find("tr")
            print "第" + str(index + 1) + "页: \n"
            for i in q:
                print q(i).text()
        driver.close()

nwd = NWD()
nwd.printPage()