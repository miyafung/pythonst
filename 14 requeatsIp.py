import requests
url="http://www.ip138.com/iplookup.asp?ip="
r =requests.get(url+'202.204.80.112')
try:
    print(r.status_code)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print("失败")
