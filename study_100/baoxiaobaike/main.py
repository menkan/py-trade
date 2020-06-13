# encoding: utf-8

import requests
from lxml import etree
import json
import time


# Requests
class RequestPage:

    def __init__(self):
        self.headers = {
            # more nothing headers...
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
        }

    def get_html(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode()


# Structure
class HTMLStructure:
    def __init__(self, context):
        self.context = context

    # created html and return;
    def created_html(self):
        ct = self.context
        return None if not ct else etree.HTML(ct)

    def handle_c_context(self):
        pass

    def handle_child(self, elements):
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
    def handle_element(self):
        ele = etree.HTML(self.context)
        result = ele.xpath('//div[@class="article block untagged mb15"]')
        return self.handle_child(result)


# CREATED OUTPUT
class OutputHtml:
    def output_html(self, lists):
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


# Hilarious
class Hilarious:
    # initialization variable
    def __init__(self):
        self.url = 'http://www.baoxiaobaike.com/p/{}'
        self.base_url = 'http://www.baoxiaobaike.com'
        # self.total = 2591
        self.total = 50
        self.pageIndex = 1

    def run(self):
        page_index = 1
        form_data = []
        total = self.total + 1

        req = RequestPage()

        while page_index < total:
            print('filter content no.%s' % page_index)
            result = req.get_html(self.url.format(page_index))
            htl = HTMLStructure(result)
            res = htl.handle_element()
            form_data.extend(res)
            page_index += 1
            time.sleep(0.2)  # 延时0.1秒; 防止对方服务器得知我们是爬虫

        str_data = json.dumps(form_data, ensure_ascii=False)
        print(str_data)
        # with open('example.json', 'w', encoding="utf-8") as f:
        #     f.write(str_data)

        # self.createdHtml(form_data)
        print('='*60)
        print('over form data')


if __name__ == '__main__':
    example = Hilarious()
    example.run()

