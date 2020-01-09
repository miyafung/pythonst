import requests

kv = {'wd': 'miyafen'}
try:
    r = requests.get("https://www.baidu.com", params=kv)
    print(r.status_code)
    print(r.request.url)
except:
    print("爬取失败")