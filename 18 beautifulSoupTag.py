from bs4 import BeautifulSoup
import requests

linka = requests.get("http://www.baidu.com")

p = linka.text

soup = BeautifulSoup(p,"html.parser")

print(soup.prettify())
