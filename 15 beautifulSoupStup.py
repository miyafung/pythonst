import requests
from bs4 import BeautifulSoup #导入库

r=requests.get("http://www.opticres.com")
print(r.status_code)
demo = r.text
# print(demo)
soup = BeautifulSoup(demo,"html.parser")
print(soup.prettify())#解析