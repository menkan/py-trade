# encoding: utf-8

# @Created by menkan on 20200602
# @Description about requests modules.

"""
# request props
timeout

new module => retrying
pip install retrying

from retrying import retry
example:

@retry(stop_max_attempt_number=3) # 让被执行的函数执行三次、如成功继续往后走；
def default():
    print('xxx')
    raise ValueError('this is test error')
"""
# import requests

# cookie = 'key=val; key=val; key=val...'
# cookie_dist = {
#     i.split('=')[0]: i.split('=')[-1] for i in [],
# }

# result = requests.get('http://www.renren.com/')
# with open('rr.html', 'w', encoding='utf-8') as f:
#     f.write(result.content.decode())


'''
# request.sessiion # 会话保持操作...
session = request.session()
session.post(...)
'''

'''
# 数据提取方法
import json
json.loads # 把json字符串转换成
jsn.dump # 把dist转换成str
    dump(dist, ensure_ascii=False, indent=2) # 不把文字转换成编码保存 # 保存时第二行比第一行空两格...
'''

'''
# xpath and lxml
# xpath 一门从html中提取数据的语言
  xpath语法 > xpath helper 插件 帮助我们从element中定位数据
  
'''


# Query Datas
# desc: 获取数据格式;
# result = requests.get('https://tianqi.moji.com/weather/china/shanghai/putuo-district')
# print(result.text)