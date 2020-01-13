import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.opticres.com")
t = r.text
print(r.status_code)
print(t[:100])




