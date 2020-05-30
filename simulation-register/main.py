# encoding: utf-8
# Created by menkan on 20200528
# Email: xtz17515@163.com

# test 1

# need -> pip install requests

import requests

ORIGINHREF = 'https://www.baidu.com'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"
}

response = requests.get(ORIGINHREF, headers=headers)

print(response.content.decode())

