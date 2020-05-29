#coding:utf8

# Created by menkan on 2019.
# Email: xtz17515@163.com
import re
import urllib
from urllib.request import Request, urlopen, urlretrieve
# form urllib import urlretrieve

# ConstName
IMG_PREFIX = "photo-"
# origin href of BaiDu Tieba
# default 1
ORIGIN_HREF = "https://tieba.baidu.com/p/4364768066?pn="
PAGENUM = 1

ImageName = IMG_PREFIX + 'page-' + str(PAGENUM)
origi_herf = ORIGIN_HREF + str(PAGENUM)

print('='*66)


# get html code <html>...</html>
def get_html_code(href):
    code = urlopen(href)
    html = code.read().decode('utf-8')
    return html


# queyr <img...> in html code
def query_images_list(code):
    regex = r'<img\s?class="BDE_Image"\s*?src="(.+?\.jpg)"'
    return re.findall(regex, code)


htmlCode = get_html_code(origi_herf)

if htmlCode:
    lists = query_images_list(htmlCode)
    print("Images total: %s" % len(lists))
else:
    print('Error: href Error, please confirm link address')
    exit()


# Download img
count = 0
for imgPath in lists:
    urlretrieve(imgPath, "./Downloads/" + ImageName + "_%d.jpg" % (count + 1))
    print("%2d picture img download over..." % count)
    count += 1

print('='*66)
print('download successful! $ cd ./Downloads/')
print('='*66)
