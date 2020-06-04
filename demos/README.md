
### xpath and lxml

> xpath 一门从html中提取数据的语言

> xpath语法 > xpath helper 插件 帮助我们从element中定位数据
>

1. 选择节点（标签）
    -   `/html/head/mate`  能选择目录下所有
    - `//li` 能全局任意选择标签
    - `/div[@class='className']/ul/li` div class名字为classname 下的ul>li
    - `//@href`
    - `/a/text()`
    - `/a//text()`
    - `./` 表示当前

#### use lxml

`pip install lxml`

```python
from lxml import etree

# transform to html
element = etree.HTML("html string")
result = element.xpath("...")
print(result)
```
