# encoding: utf-8

# import package.

import sys
import re
from typing import NamedTuple

# import requests
# from lxml import etree
# import json
# import time

# myself module
from brower_c import Brower

brower_header = Brower()._chameleon()

# website link.
baseUrl = 'https://www.biquge7.com/book/199/'

'''
书写流程概要.
当前页面Url.
根据url取获取当前页面(模拟PC请求页面；防止过多广告)全部html内容。
通过etree过滤html保留 标题，正文，上一页，下一页等内容;
当点击上/下一页的时候
'''

# 获取链接所有内容
class GetHtml:
    # 获取全部Html内容
    def get_all_html(self):
        pass

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
            link = baseUrl
            print('执行内部 Link. %s' % link)

        elif lengs == 2:
            link = args[1]
            print('执行外部传入verable link. %s' % link)

        else:
            self.out_command()

        self.step1(link)
    
    # step1.
    # 检查地址.
    def step1(self, link):
        # check link is comfirm.
        bool = self._check_link_isconfirm(link)

        if not bool:
            self.out_command()

        # 获取全部数据内容
        self.get_html_t = GetHtml()

    
    # check lin is confirm.
    def _check_link_isconfirm(self, link) -> bool:
        regexp = r'^http[s]?://.*'
        res = re.match(regexp, link)
        if res:
            print('link okay.')
            return True
        else:
            self.out_command()

    # out command.
    def out_command(self):
        print('| End | program error. exit()')
        exit()


if __name__ == '__main__':
    Main()
