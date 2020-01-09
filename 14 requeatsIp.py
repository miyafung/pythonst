import requests
url="http://www.ip138.com/iplookup.asp?ip="
r =requests.get(url+'192.168.18.1')
try:
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[-500:])
except:
    print("失败")