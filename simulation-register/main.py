# encoding: utf-8
# Created by menkan on 20200528
# Email: xtz17515@163.com
# @Description: 命令行版中文转英文翻译；
# 参考： https://blog.csdn.net/weixin_40074227/article/details/104238335
# need -> pip install requests, PyExecJS

import requests
import re
import execjs


def get_sign(w, g):
    with open('index.js') as f:
        jsdata = f.read()
    ctx = execjs.compile(jsdata)
    return ctx.call('e', w, g)


def get_token(result):
    token = re.findall(r"token: '(.*?)',", result)
    gtk = re.findall(r"window.gtk = '(.*?)';", result)
    if token and gtk:
        return token[0], gtk[0]


if __name__ == '__main__':
    session = requests.session()

    url = 'https://fanyi.baidu.com/'

    response = session.post(url)
    response = session.post(url)

    token, gtk = get_token(response.text)

    headers = {
        "Rerer": "https://fanyi.baidu.com/",
        "User-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36",
    }
    # chinese => english
    print('输入中文-翻译成英文：\n')
    word = input("：")

    if not word:
        print('请输入内容')
        exit()

    sign = get_sign(word, gtk)
    data = {
        "from": 'zh',
        "to": "en",
        "query": word,
        "simple_means_flag": '3',
        "sign": sign,
        "token": token,
    }
    session.post(url='https://fanyi.baidu.com/langdatect', data={'query': word})
    res = session.post(url="https://fanyi.baidu.com/v2transapi?from=en&to=jp", data=data, headers=headers)
    print(res.json()['trans_result']['data'][0]['dst'])
    # while True:
    # 可以做成一直循环查内容的
    # print("Result:", res.json()['trans_result']['data'][0])
