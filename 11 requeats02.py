import requests

r = requests.head("http://wwww.baidu.com")
print(r.status_code)
print(r.encoding)
print(r.headers)
 #显示中文print(r.text[:20])
r.encoding = 'UTF-8'
print(r.text)