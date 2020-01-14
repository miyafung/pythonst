import requests
import re

#获得页面的函数

def getHTMLText(url):
    print("")

def parsePage(ilt,html):
    print()

def printGoodsList(ilt):
    print()

def main():
    goods = '鼠标'
    depth = 2
    start_url = 'https://s.taobao.com/search?q=' + goods
    infoList = []

#由于分页，需要进行循环
    for i in range(depth):
        try:
            url = start_url + '$s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodsList(infoList)
main()