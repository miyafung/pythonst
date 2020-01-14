from bs4 import BeautifulSoup
import requests
import re
#re 是正则表达式
linka = requests.get("http://www.baidu.com")
p = linka.text
soup = BeautifulSoup(p,"html.parser")

#find_all 方法
# soupa = soup.find_all('img')

for tag in soup.find_all(re.compile('p')): #查找还有P的标签
    print(tag.name)


