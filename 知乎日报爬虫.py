# encoding=utf-8

import urllib.request
import re
from html.parser import HTMLParser  #实现html文件的分析解析过程
import requests    #
import sys
import importlib
importlib.reload(sys)

url = "https://daily.zhihu.com/"
#获取源码
def getHtml(url):
    header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"}
    response = urllib.request.urlopen(url)
    text = response.read() #获取源码
    text = text.decode('utf-8')  # python3


    #print (text)
    return text



#解析每一条日报的超链接
def getUrls(html):
    pattern = re.compile('<a href="/story/(.*?)"',re.S) #提高效率
    items = re.findall(pattern,html)
    #print (items) #list
    #return items
    urls = [] #拼接好的连接
    for item in items :
        urls.append('https://daily.zhihu.com/story/'+item)
        #print (urls[-1])

    return urls

#解析日报标题+正文
def getContent(url,items_whole):
    html = getHtml(url)  #调用函数
    pattern = re.compile('<title>(.*?)</title>',re.S)
    items = re.findall(pattern,html)
    #print(items[0])
    pattern = re.compile('<div class="content">\\n<p>(.*?)</div>',re.S)
    items_withtag = re.findall(pattern,html)
    #print(items_withtag[0])
    items_whole.append('#############################################################################')
    items_whole.append(items[0])
    items_whole.append('#############################################################################')
    items_whole.append(items_withtag[0])

    #print(len(items())
    #print(len(items_withtag))
    #print(items_whole)

    return items_whole


items_whole = []
html = str(getHtml(url)) #调用
urls = getUrls(html)
#print (urls)
for url in urls:
    try:
        getContent(url,items_whole) #获取超链接的文本内容
    except Exception as e:
        print (e)


itemss = getContent(url,items_whole)
itemss = itemss.unicode('gbk')
word = open('word.txt', 'w')
for i in range(len(itemss)):
    word.write(itemss[i])
#print(itemss)

word.close()

'''a = ['1','2','3','4','5']
b = ['1','2','3','4','5']
c = []

for i in range(len(a)):
    c.append(a[i])
    c.append(b[i])

print (c)'''
