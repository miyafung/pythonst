import requests
from lxml import etree
import time
import csv

# 定义函数抓取每页前30条商品信息
def crow_first(n):
    # 构造每一页的url变化
    url = 'https://search.jd.com/Search?keyword=dell%E5%8F%B0%E5%BC%8F%E6%9C%BA&enc=utf-8&page=' + str(
        2 * n - 1)
    head = {'authority': 'search.jd.com',
            'method': 'GET',
            'path': '/s_new.php?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=4&s=84&scrolling=y&log_id=1529828108.22071&tpl=3_M&show_items=7651927,7367120,7056868,7419252,6001239,5934182,4554969,3893501,7421462,6577495,26480543553,7345757,4483120,6176077,6932795,7336429,5963066,5283387,25722468892,7425622,4768461',
            'scheme': 'https',
            'referer': 'https://search.jd.com/Search?keyword=dell%E5%8F%B0%E5%BC%8F%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&bs=1&suggest=7.def.0.V00--11s0%2C19s0%2C38s0%2C96s0&wq=Dell&ev=exbrand_%E6%88%B4%E5%B0%94%EF%BC%88DELL%EF%BC%89%5E&page=5&s=116&click=0',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'Cookie': 'qrsc=3; pinId=RAGa4xMoVrs; xtest=1210.cf6b6759; ipLocation=%u5E7F%u4E1C; _jrda=5; TrackID=1aUdbc9HHS2MdEzabuYEyED1iDJaLWwBAfGBfyIHJZCLWKfWaB_KHKIMX9Vj9_2wUakxuSLAO9AFtB2U0SsAD-mXIh5rIfuDiSHSNhZcsJvg; shshshfpa=17943c91-d534-104f-a035-6e1719740bb6-1525571955; shshshfpb=2f200f7c5265e4af999b95b20d90e6618559f7251020a80ea1aee61500; cn=0; 3AB9D23F7A4B3C9B=QFOFIDQSIC7TZDQ7U4RPNYNFQN7S26SFCQQGTC3YU5UZQJZUBNPEXMX7O3R7SIRBTTJ72AXC4S3IJ46ESBLTNHD37U; ipLoc-djd=19-1607-3638-3638.608841570; __jdu=930036140; user-key=31a7628c-a9b2-44b0-8147-f10a9e597d6f; areaId=19; __jdv=122270672|direct|-|none|-|1529893590075; PCSYCityID=25; mt_xid=V2_52007VwsQU1xaVVoaSClUA2YLEAdbWk5YSk9MQAA0BBZOVQ0ADwNLGlUAZwQXVQpaAlkvShhcDHsCFU5eXENaGkIZWg5nAyJQbVhiWR9BGlUNZwoWYl1dVF0%3D; __jdc=122270672; shshshfp=72ec41b59960ea9a26956307465948f6; rkv=V0700; __jda=122270672.930036140.-.1529979524.1529984840.85; __jdb=122270672.1.930036140|85.1529984840; shshshsID=f797fbad20f4e576e9c30d1c381ecbb1_1_1529984840145'
            }
    r = requests.get(url, headers=head)
    # 指定编码方式，不然会出现乱码
    r.encoding = 'utf-8'
    html1 = etree.HTML(r.text)
    # 定位到每一个商品标签li
    datas = html1.xpath('//li[contains(@class,"gl-item")]')

    '''抓评论'''
    pids = html1.xpath('//li[contains(@class,"gl-item")]/attribute::data-pid')
    comment_url = "https://club.jd.com/comment/productCommentSummaries.action?referenceIds="
    for pid in pids:
        comment_url += pid + ","
    comment_r = requests.get(comment_url)
    p_comment = []
    for comment in comment_r.json()["CommentsCount"]:
        p_comment.append([comment["CommentCount"], comment["AverageScore"],
                          comment["GoodCount"], comment["DefaultGoodCount"],
                          comment["GoodRate"], comment["AfterCount"], comment["VideoCount"],
                          comment["PoorCount"], comment["GeneralCount"]])
        # 总评数，平均得分，好评数，默认好评，好评率，追评数，视频晒单数，差评数，中评数

    # 将抓取的结果保存到本地CSV文件中
    with open('JD_Phone.csv', 'a', newline='', encoding='gb18030')as f:
        write = csv.writer(f)
        i = 0
        for data in datas:
            p_price = data.xpath('div/div[@class="p-price"]/strong/i/text()')
            p_name = data.xpath('div/div[@class="p-name p-name-type-2"]/a/em')
            # 这个if判断用来处理那些价格可以动态切换的商品，比如上文提到的小米MIX2，他们的价格位置在属性中放了一个最低价
            if len(p_price) == 0:
                p_price = data.xpath('div/div[@class="p-price"]/strong/@data-price')
                # xpath('string(.)')用来解析混夹在几个标签中的文本
            write.writerow([p_name[0].xpath('string(.)'), p_price[0], p_comment[i][0], p_comment[i][1], p_comment[i][2],
                            p_comment[i][3], p_comment[i][4], p_comment[i][5], p_comment[i][6], p_comment[i][7],
                            p_comment[i][8]])
            i += 1
    f.close()


# 定义函数抓取每页后30条商品信息
def crow_last(n):
    # 获取当前的Unix时间戳，并且保留小数点后5位
    a = time.time()
    b = '%.5f' % a
    url = 'https://search.jd.com/Search?keyword=dell%E5%8F%B0%E5%BC%8F%E6%9C%BA&enc=utf-8&page=' + str(
        2 * n) + '&s=' + str(48 * n - 20) + '&scrolling=y&log_id=' + str(b)
    head = {'authority': 'search.jd.com',
            'method': 'GET',
            'path': '/s_new.php?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA',
            'scheme': 'https',
            'referer': 'https://search.jd.com/Search?keyword=dell%E5%8F%B0%E5%BC%8F%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&bs=1&suggest=7.def.0.V00--11s0%2C19s0%2C38s0%2C96s0&wq=Dell&ev=exbrand_%E6%88%B4%E5%B0%94%EF%BC%88DELL%EF%BC%89%5E&page=5&s=116&click=0',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'Cookie': 'qrsc=3; pinId=RAGa4xMoVrs; xtest=1210.cf6b6759; ipLocation=%u5E7F%u4E1C; _jrda=5; TrackID=1aUdbc9HHS2MdEzabuYEyED1iDJaLWwBAfGBfyIHJZCLWKfWaB_KHKIMX9Vj9_2wUakxuSLAO9AFtB2U0SsAD-mXIh5rIfuDiSHSNhZcsJvg; shshshfpa=17943c91-d534-104f-a035-6e1719740bb6-1525571955; shshshfpb=2f200f7c5265e4af999b95b20d90e6618559f7251020a80ea1aee61500; cn=0; 3AB9D23F7A4B3C9B=QFOFIDQSIC7TZDQ7U4RPNYNFQN7S26SFCQQGTC3YU5UZQJZUBNPEXMX7O3R7SIRBTTJ72AXC4S3IJ46ESBLTNHD37U; ipLoc-djd=19-1607-3638-3638.608841570; __jdu=930036140; user-key=31a7628c-a9b2-44b0-8147-f10a9e597d6f; areaId=19; __jdv=122270672|direct|-|none|-|1529893590075; PCSYCityID=25; mt_xid=V2_52007VwsQU1xaVVoaSClUA2YLEAdbWk5YSk9MQAA0BBZOVQ0ADwNLGlUAZwQXVQpaAlkvShhcDHsCFU5eXENaGkIZWg5nAyJQbVhiWR9BGlUNZwoWYl1dVF0%3D; __jdc=122270672; shshshfp=72ec41b59960ea9a26956307465948f6; rkv=V0700; __jda=122270672.930036140.-.1529979524.1529984840.85; __jdb=122270672.1.930036140|85.1529984840; shshshsID=f797fbad20f4e576e9c30d1c381ecbb1_1_1529984840145'
            }
    r = requests.get(url, headers=head)
    r.encoding = 'utf-8'
    html1 = etree.HTML(r.text)
    datas = html1.xpath('//li[contains(@class,"gl-item")]')

    '''抓评论'''
    pids = html1.xpath('//li[contains(@class,"gl-item")]/attribute::data-pid')
    comment_url = "https://club.jd.com/comment/productCommentSummaries.action?referenceIds="
    for pid in pids:
        comment_url += pid + ","
    comment_r = requests.get(comment_url)
    p_comment = []
    for comment in comment_r.json()["CommentsCount"]:
        p_comment.append([comment["CommentCount"], comment["AverageScore"],
                          comment["GoodCount"], comment["DefaultGoodCount"],
                          comment["GoodRate"], comment["AfterCount"], comment["VideoCount"],
                          comment["PoorCount"], comment["GeneralCount"]])
        # 总评数，平均得分，好评数，默认好评，好评率，追评数，视频晒单数，差评数，中评数

    with open('JD_Phone.csv', 'a', newline='', encoding='gb18030')as f:
        write = csv.writer(f)
        i = 0
        for data in datas:
            p_price = data.xpath('div/div[@class="p-price"]/strong/i/text()')
            p_name = data.xpath('div/div[@class="p-name p-name-type-2"]/a/em')
            if len(p_price) == 0:
                p_price = data.xpath('div/div[@class="p-price"]/strong/@data-price')
            write.writerow([p_name[0].xpath('string(.)'), p_price[0], p_comment[i][0], p_comment[i][1], p_comment[i][2],
                            p_comment[i][3], p_comment[i][4], p_comment[i][5], p_comment[i][6], p_comment[i][7],
                            p_comment[i][8]])
            i += 1
    f.close()

if __name__ == '__main__':
    for i in range(1, 3):
        print('***************************************************')
        try:
            print('   First_Page:   ' + str(i))
            crow_first(i)
            print('   Finish')
        except Exception as e:
            print(e)
        print('------------------')
        try:
            print('   Last_Page:   ' + str(i))
            crow_last(i)
            print('   Finish')
        except Exception as e:
            print(e)