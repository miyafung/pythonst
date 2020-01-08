import requests
r = requests.get("http://www.baidu.com")
print(r.status_code)
# 200 状态码表示访问成功
print(r.encoding)

r.encoding = "utf-8"
print(r.text)