# encoding: utf-8


# import package.

import requests

from lxml import etree

import json

import time

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
    pass

if __name__ == '__main__':
    # 执行数据内容.
    pass