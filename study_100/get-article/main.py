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
class Chameleon:
    def __init__(self) -> None:
        pass
    
    def _set_header(self):
        header = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Cache-Control": "max-age=0",
            "Host": "m.bswtan.com", # 模拟的host网址.
            "Accept-Language": "zh-CN,zh;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        }
        return header


class Main:
    pass


def check_link_isconfirm(link) -> bool:
    # baseUrl = 'http://m.bswtan.com/43/43127/'
    regexp = r'^http[s]://\w*.\w*.com/\d*/\d*/$'
    res = re.match(regexp, link)
    if res:
        pass
    else:
        print('Invalid Link.')
        exit()


# initization.
def init():
    args = sys.argv
    lengs = len(args)
    if lengs == 1:
        link = baseUrl
        print('执行内部constant.')
    elif lengs == 2:
        link = args[2]
        print('执行外部传入verable')
    else:
        print('Error input txt')
        exit()

if __name__ == '__main__':
    init()