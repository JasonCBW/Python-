# coding=utf-8

import urllib2
import cookielib

#设置保存cookie的文件，同级目录下的cookie.txt文件
filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookies = cookielib.MozillaCookieJar(filename)
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookies)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
#此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open('http://www.baidu.com')

cookies.save(ignore_discard=True, ignore_expires=True)
for item in cookies:
    print 'Name = ' + item.name
    print 'Value = ' + item.value


