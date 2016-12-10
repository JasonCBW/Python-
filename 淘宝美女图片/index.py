# coding:utf-8

import urllib
import urllib2
import os
import json
import re

class Tool:
    # 去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    # 删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    # 把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # 将表格制表<td>替换为\t
    replaceTD = re.compile('<td>')
    # 把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    # 将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    # 将其余标签剔除
    removeExtraTag = re.compile('<.*?>')

    def replace(self, html):
        html = re.sub(self.removeImg, "", html)
        html = re.sub(self.removeAddr, "", html)
        html = re.sub(self.replaceLine, "\n", html)
        html = re.sub(self.replaceTD, "\t", html)
        html = re.sub(self.replacePara, "\n    ", html)
        html = re.sub(self.replaceBR, "\n", html)
        html = re.sub(self.removeExtraTag, "", html)
        return html.strip()

class Spider:

    def __init__(self, size):
        self.baseURL = 'https://mm.taobao.com/json/request_top_list.htm'
        #大图
        self.showSize = size
        self.txtPath = u"个人信息"
        self.picPath = u"个人图片"
        self.tool = Tool()

    def getPage(self, pageIndex):
        url = self.baseURL + "?page=" + str(pageIndex)
        req = urllib2.Request(url)
        res = urllib2.urlopen(req)
        content = res.read().decode('gbk')
        return content

    def getContents(self, pageIndex):
        pageContent = self.getPage(pageIndex)
        pattern = re.compile('<div class="list-item".*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>', re.S)
        items = re.findall(pattern, pageContent)
        contents = []
        for item in items:
            infoUrl = re.findall(r'[0-9]', item[0])
            imgUrl = item[1]
            infoUrl = ('').join(infoUrl)
            infoUrl = "https://mm.taobao.com/self/model_info.htm?user_id=" + infoUrl + "&is_coment=false"
            if self.showSize == 1:
                imgUrl = imgUrl[0:imgUrl.rindex('_')]
            contents.append([item[2], item[3], item[4], infoUrl, "http:" + imgUrl])
        return contents

    def getDetailPage(self, infoUrl):
        res = urllib2.urlopen(infoUrl)
        content = res.read().decode('gbk')
        return content


    def saveImgs(self, images, name):
        number = 1
        print u"发现", name, u"共有", len(images), u"张照片"
        for imageUrl in images:
            splitPath = imageUrl.split('.')
            fTail = splitPath.pop()
            if len(fTail) > 3:
                fTail = "jpg"
            fileName = name + "/" + str(number) + "." + fTail
            self.saveImg(imageUrl, fileName)
            number += 1

    def saveImg(self, imageUrl, name):
        u = urllib.urlopen(imageUrl)
        data = u.read()
        fileName = self.picPath + "/" + name + ".jpg"
        f = open(fileName, 'wb')
        f.write(data)
        print u"正在悄悄保存她的一张图片为", fileName
        f.close()

    def saveBrief(self, content, name):
        fileName = self.txtPath + "/" + name + ".txt"
        f = open(fileName, "w+")
        print u"正在偷偷保存她的个人信息为", fileName
        f.write(content.encode('utf-8'))

    def mkdir(self):
        txtIsExists = os.path.exists(self.txtPath)
        picIsExists = os.path.exists(self.picPath)
        if not txtIsExists:
            print u"偷偷新建了名字叫做", self.txtPath, u"的文件夹"
            os.makedirs(self.txtPath)
        if not picIsExists:
            print u"偷偷新建了名字叫做", self.picPath, u"的文件夹"
            os.makedirs(self.picPath)


    def savePageInfo(self, pageIndex):
        contents = self.getContents(pageIndex)
        for item in contents:
            print u"发现一位模特，名字叫", item[0], u"芳龄", item[1], u"她在", item[2]
            print u"正在偷偷地保存", item[0], u"的信息"
            print u"又意外地发现她的个人地址是", str(item[3])
            detailUrl = item[3]

            self.mkdir()
            brief = self.getDetailPage(detailUrl)
            #保存文本
            self.saveBrief(brief, item[0])
            # 保存图片
            self.saveImg(item[4], item[0])

    def savePagesInfo(self, start, end):
        for i in range(start, end + 1):
            print u"正在偷偷寻找第", i, u"个地方，看看MM们在不在"
            self.savePageInfo(i)

spider = Spider(1)
spider.savePagesInfo(1, 40)
