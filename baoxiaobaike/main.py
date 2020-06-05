# encoding: utf-8

import requests
from lxml import etree
import json

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36",
    # "Referer": "http://www.baoxiaobaike.com/p/1",
    # "Accept-Encoding": "gzip, deflate",
    # "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    # "Cache-Control": "max-age=0",
    # "Connection": "keep-alive",
    # "Host": "www.baoxiaobaike.com",
    # "Upgrade-Insecure-Requests": '1',
    # "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    # "Cookie": "PHPSESSID=f293dp368plfc45c6ai46qdv17; Hm_lvt_736f3cc4020964c0f4c3db8bbd3a5336=1591368363; Hm_lpvt_736f3cc4020964c0f4c3db8bbd3a5336=1591371886"
}


class Hilarious:

    def __init__(self):
        self.url = 'http://www.baoxiaobaike.com/p/{}'
        self.baseurl = 'http://www.baoxiaobaike.com'
        self.total = 2591
        self.pageIndex = 1

    def gethtml(self, url):
        response = requests.get(url, headers=headers)
        return response.content.decode()

    def handleChildrenEle(self, elements):
        list = []
        for element in elements:
            imgs = element.xpath('./div[@class="content"]//img/@src')
            list.append({
                "title": element.xpath('./div[@class="title"]/a/text()'),
                "content": element.xpath('./div[@class="content"]//p/text()'),
                "imgs": imgs if len(imgs) else ''
            })
        return list

    # 获取每一块内容返回 list[dist]
    def handleElement(self, element):
        ele = etree.HTML(element)
        result = ele.xpath('//div[@class="article block untagged mb15"]')
        return self.handleChildrenEle(result)

    def run(self):
        result = self.gethtml(self.url.format(1))
        res = self.handleElement(result)
        str = json.dumps(res, ensure_ascii=False)
        with open('example.json', 'w', encoding="utf-8") as f:
            f.write(str)
        # print(res)


if __name__ == '__main__':
    example = Hilarious()
    example.run()

