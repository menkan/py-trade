[TOC]

# 小记

> python 是一门动态语言。 

## py类型

* 整数 int
    - 可以通过`_`去分割特别大的数字 100000 => 10_0000;
    - 十六进制也可以如此
* 浮点数 float
    - 可以用科学计数法表示`1.23e9`
* 字符串 string
    - 用单引号或双引号括包裹起来的任意文本内容
* 布尔值 Boolean - True&False
    - and、or、not 运算符。
* None 表示空值-非0;特殊的空值
* list
* tuple
* dict
* set



###### 除法

```pythone

10 / 3
: 3.33*

9/3
: 3.0

9//3
: 3

//  表示地板除
取余 % 返回的也是整数

```

``变量``
可变的量;


``常量``

> python 中用大写字母表示常量内容 `PI = 3.14`

不可变的量


## 字符编码

> 默认字符编码`ASCII`编码； 一个字节

> 后因各种问题出现了`Unicode`字符集； 两个字节

```python
ord('A') # 65
chr(65) # A

* Python对bytes类型的数据用带b前缀的单引号或双引号表示：
x = b'ABC'

'ABC'.encode('ascii'/'utf-8')
b'abc'.decode('utf-8', errors='ignore')
# 可以传入errors='ignore'去屏蔽错误

len('string') # 包含多少字符
# 统计字符的个数。 如果是bytes格式统计在内存中占了几个字节;


# 为保证python能正确解析。 
# 在文件头部书写格式确定
# ------
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

```

### 格式化输出文本。
> 与C语言相似

```python
>>> 'Hello, %s' % 'world'
'Hello, world'

>>> 'Hi, %s, you have $%d.' % ('Michael', 1000000)
'Hi, Michael, you have $1000000.'

```

Placeholder|Desc|
:---|---|
%d|整数
%s|字符串
%f|浮点数
%x|十六进制整数

> 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串

```python

format()
>>> 'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)
'Hello, 小明, 成绩提升了 17.1%'


f-string
# 最后一种格式化字符串的方法是使用以f开头的字符串，称之为f-string，它和普通字符串不同之处在于，字符串如果包含{xxx}，就会以对应的变量替换：

>>> r = 2.5
>>> s = 3.14 * r ** 2
>>> print(f'The area of a circle with radius {r} is {s:.2f}')
The area of a circle with radius 2.5 is 19.62
```

### List And tuple

> list 是一组有序的集合。 Js中的数组