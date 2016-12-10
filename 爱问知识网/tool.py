# coding:utf-8

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