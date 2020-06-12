# encoding: utf-8

import requests
from lxml import etree
import json
import time

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
        # self.total = 2591
        self.total = 50
        self.pageIndex = 1

    def gethtml(self, url):
        response = requests.get(url, headers=headers)
        return response.content.decode()

    def handleChildrenEle(self, elements):
        lists = []
        for element in elements:
            imgs = element.xpath('./div[@class="content"]//img/@src')
            lists.append({
                "title": element.xpath('./div[@class="title"]/a/text()'),
                "content": element.xpath('./div[@class="content"]//p/text()'),
                "imgs": imgs if len(imgs) else ''
            })
        return lists

    # 获取每一块内容返回 list[dist]
    def handleElement(self, element):
        ele = etree.HTML(element)
        result = ele.xpath('//div[@class="article block untagged mb15"]')
        return self.handleChildrenEle(result)

    def createdHtml(self, lists):
        print(len(lists))
        start = r'<html><head><meta charset="utf-8" /></head><body>'
        end = r'</body></html>'
        context = ''

        for item in lists:
            context += '<div class="item">'
            context += '<div class="item__title"><h3>{}</h3></div>'.format(item['title'][0])
            if len(item['content']):
                context += '<div class="context">'
                for con in item['content']:
                    context += '<p>{}</p>'.format(con)
                context += '</div>'
            if item['imgs']:
                for img in item['imgs']:
                    context += '<img src="' + self.baseurl + '{}" />'.format(img)
            context += '</div>'
        with open('index.html', 'w', encoding="utf-8") as f:
            f.write(start + context + end)
        print('html加载完成...')

    def run(self):
        page_index = 1
        form_data = []
        total = self.total + 1

        while page_index < total:
            print('filter content no.%s' % page_index)
            result = self.gethtml(self.url.format(page_index))
            res = self.handleElement(result)
            form_data.extend(res)
            page_index += 1
            time.sleep(0.2)  # 延时0.1秒; 防止对方服务器得知我们是爬虫

        str_data = json.dumps(form_data, ensure_ascii=False)
        with open('example.json', 'w', encoding="utf-8") as f:
            f.write(str_data)

        self.createdHtml(form_data)
        print('='*60)
        print('over form data')


if __name__ == '__main__':
    example = Hilarious()
    example.run()

