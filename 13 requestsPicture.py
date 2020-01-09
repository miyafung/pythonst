import requests
import os
path ="C:/Users/miya/Desktop/test/abc.jpg"
url ="https://www.opticres.com/Public/Uploads/small/5cef4b4acff0e.jpg"
r=requests.get(url)
print(r.status_code)

with open(path,'wb') as f:
    k=f.write(r.content)
    print(k)
