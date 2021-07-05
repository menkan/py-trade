# encoding: utf-8

# import package.

import sys
import re
from typing import Counter

import requests
# from lxml import etree
# import json
# import time


# myself module
from brower_c import Brower

brower_header = Brower()._chameleon()

# website link.
base_origin = 'https://www.biquge7.com'

base_path = '/book/199/'

'''
书写流程概要.
当前页面Url.
根据url取获取当前页面(模拟PC请求页面；防止过多广告)全部html内容。
通过etree过滤html保留 标题，正文，上一页，下一页等内容;
当点击上/下一页的时候
'''

# COMMON Class;
class Common:
    def out_command(self):
        print('| system | out |　process error exit.')
        exit()
    
    def out_error(self, content):
        print('| Error | ' + content)
        self.out_command()

common = Common()

# 获取链接所有内容
class GetHtml:
    def __init__(self, link) -> None:
        self.link = link

    # 获取全部Html内容
    def get_all_html(self):
        response = requests.get(base_origin + base_path, headers=brower_header)
        if response.status_code == 200:
            print('1')
        else:
            print('2')

    # 获取关键内容
    def get_part_html(self):
        pass


class Main:
    # self
    result = '' # 全部内容。
    get_html_t = None

    # initiation
    def __init__(self) -> None:
        args = sys.argv
        lengs = len(args)

        if lengs == 1:
            link = base_origin + base_path
            print('执行内部 Link. %s' % link)

        elif lengs == 2:
            link = args[1]
            print('执行外部传入verable link. %s' % link)

        else:
            common.out_command()

        self.step1(link)
    
    # step1.
    # 检查地址.
    def step1(self, link):
        # check link is comfirm.
        bool = self._check_link_isconfirm(link)

        if not bool:
            common.out_command()

        # 获取全部数据内容
        self.get_html_t = GetHtml().get_all_html()


    
    # check lin is confirm.
    def _check_link_isconfirm(self, link) -> bool:
        regexp = r'^http[s]?://.*'
        res = re.match(regexp, link)
        if res:
            print('link okay.')
            return True
        else:
            common.out_command()


if __name__ == '__main__':
    Main()
