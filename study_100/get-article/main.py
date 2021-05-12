# encoding: utf-8


# import package.

import sys
import re
# import requests
# from lxml import etree
# import json
# import time

# website link.
baseUrl = 'http://m.bswtan.com/43/43127/'

# >>>>>>>

'''
书写流程概要.

当前页面Url.

根据url取获取当前页面(模拟PC请求页面；防止过多广告)全部html内容。
通过etree过滤html保留 标题，正文，上一页，下一页等内容;

当点击上/下一页的时候

'''

# 获取链接所有内容
class GetHtml:

    def __init__(self):
        pass

    # 获取全部Html内容
    def get_all_html(self):
        pass

    # 获取关键内容
    def get_part_html(self):
        pass

# 模拟 Pc Client User
def _chameleon() -> dict:
    return {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Cache-Control": "max-age=0",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "Host": "m.bswtan.com",
    }

class Main:
    # initiation
    def __init__(self) -> None:
        args = sys.argv
        lengs = len(args)
        if lengs == 1:
            link = baseUrl
            print('执行内部constant. %s' % link)
            self.step1(link)
        elif lengs == 2:
            link = args[1]
            print('执行外部传入verable, >>> %s' % link)
            self.step1(link)
        else:
            print('Error input txt')
            self.out_command()
    
    # step1.
    def step1(self, link):
        print(self._check_link_isconfirm(link))
        pass
    
    # out command.
    def out_command(self):
        print('| End | program error. exit()')
        exit()

    # check lin is confirm.
    def _check_link_isconfirm(self, link) -> bool:
        regexp = r'^http[s]?://\w*.\w*.com/\d*/\d*/$'
        res = re.match(regexp, link)
        if res:
            print('link okay.')

        else:
            print('Invalid Link.')
            self.out_command()

        return True if res else False



if __name__ == '__main__':
    Main()