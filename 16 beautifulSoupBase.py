import requests
from bs4 import BeautifulSoup #标签树
demo = requests.get("https://www.baidu.com")
print(demo.status_code)


demo.encoding
soup =BeautifulSoup(demo,"html.parser")
print(soup.title)