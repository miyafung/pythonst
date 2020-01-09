import requests

r = requests.get("https://item.jd.com/100004840977.html")
print(r.status_code)
print(r.encoding)
print(r.headers)
 #显示中文print(r.text[:20])
# r.encoding = 'UTF-8'
print(r.text[:1000])