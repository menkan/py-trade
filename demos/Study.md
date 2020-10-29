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

> list 是一组*有序*的*集合*。 Js中的数组

```python
# list attribute.

[].append(content)
[].insert(idx, content) # 指定位置插入数据

[].pop() # 尾端删除内容
[].pop(idx) # 指定位置删除内容
```

```python 
# tuple 也叫元组
# WARNNING: 是一个不可变元组 不可改变
# - 如果只定义一个字符  =>   tuple_a = (1,) # 不这样定义的话会变成数字1. 就失去了元组的特性
#: 这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义

## "可变"的 Tuple
#> 其实并没有变化分配的内存并没有变。 只是内存中的值变了而已

tuplea_a = (1, 2, [3, 4])
# 这样集合中的内容就是可变的了。

# tuple attribute.
```

### 条件判断

```python

# if
age = 18

if age >= 10:
    print('a young person')
elif age >= 3:
    print('xxx')
else:
    print('a small baby')


# input
# 命令行文本输入

> input('place input content: ')
```

### 循环

> python 循环有两种

```python

`for..in..`
    `for n in range(5)`

`while`
    break # 可以提前退出循环
    continue # 跳出本次循环前往下次循环

```
 
### dist & set 字典

> dist 全称： dictionary 或其他语言中的map或对象
使用键值对

无序字典

dist: 
查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。

而list相反：
查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。


```python
dist[key] # 不存在会报错

可以通过 key in dist 判断
或 dist.get(key, defaultValue)

# delete

dist.pop(key)

```

> set 与dist类似也是key&val集合；但不能存储val由于Key的不重复性。所以在set中没有重复的Key.

```python

s = set([1, 2, 3])
> {1, 2, 3}

s.add(key)
s.remove(key)

set 一组无顺序、无重复元素的集合

& # 交集
| # 并集

```

## 函数
> function

```python
# python 环境内置函数

help(func) # 帮助命令

abs()
max(1, 2, 3, 4) # maxValue

# 数据类型转换

int('123')
float('12.34')
str(100)
bool(1) # True
bool() # False

```

```python

# 定义函数
def func(n=2):
    # n=2 默认参数
    pass

# *可变参数。 不确定传进来的参数是多少个。 
#> 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
def func(*numbers):
    # *numbers 接受的是一个元组。不可变变量
    pass

func(1, 2, 3, 4, 5...)

num_arr=[1, 2, 3, 4...]
func(*num_arr) # 可以这样去

# ==== 关键字参数 ==== 

#> 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict 

def func(name, age, **kw):
    print('name', name, 'age', age, 'other', kw)

func('mk', 7, **dist)

# ==== 命名关键字参数 ====

def person(name, age, *, city, job):
    print(name, age, city, job)

# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。

# 可变参数后边皆是命名关键字
def person(name, age, *args, city, job):
    print('name', name, 'age', age, args, 'city', city, 'job', job)

# ==== 参数组合 ==== 
#> 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数

# 必须按照该顺序搞

也可以直接传入tuple&list&dist

# ==== 递归 ====

调用自身就是递归

递归太大会造成栈溢出。 产生报错。 
优化的话就是采用尾递归方式

```

默认参数一定要是不可变变量。 不然会出现逻辑错误
***WARNNING: 命名关键词为Python3持有***

## 高级特性

> 代码总是越精简越好

### 切片

集合切片

```python
list[0:3] # 从0始3终不包括3
list[:3] # 如果从0开始可以省略0

# 也可以倒数切片
list[-2:-1]

# 隔位取值
list[10:20:2]
12, 14, 16..

# 所有隔5切
list[::5]

# 原样复制
list[:]

list & tuple & str 皆可使用切片功能
```

### 迭代

> 通过For循环进行遍历。 俗称迭代

可迭代list & tuple & dist & set

```python
for ... in ...:
    pass

# ===========
# 如何判断一个对象是可迭代对象

# 通过 collections 模块的iterable类型check

from collections import Iterable

isinstance(obj, Iterable)
> True

# Python内置 enumerate 可以让list存在下标。

for i, value in enumerate(['a', 'b', 'c', 'd']):
    print(i, value)


集合中存在元组

ran=[(1, 2), (3, 4), (5, 6)]

for x, y in ran:
    print(x, y)

```

### 列表生成式

> 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。

```python 
>>> [x * x for x in range(1, 11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

>>> [x * x for x in range(1, 11) if x % 2 == 0]
[4, 16, 36, 64, 100]

# 双重For
>>> [m + n for m in 'ABC' for n in 'XYZ']
['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

# 列出点前目录下所有内容 => list
>>> import os # 导入os模块，模块的概念后面讲到
>>> [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
['.emacs.d', '.ssh', '.Trash', 'Adlm', 'Applications', 'Desktop', 'Documents', 'Downloads', 'Library', 'Movies', 'Music', 'Pictures', 'Public', 'VirtualBox VMs', 'Workspace', 'XCode']

# 迭代 dist.items() list 元组。
>>> dis = {'m': 'mmm', 'k': 'kkk', 'j': 'jjj'}
>>> dis.items()
[('k', 'kkk'), ('j', 'jjj'), ('m', 'mmm')]
# 列表生成式
>>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
>>> [k + '=' + v for k, v in d.items()]
['y=B', 'x=A', 'z=C']

# 首字母小写
>>> L = ['Hello', 'World', 'IBM', 'Apple']
>>> [s.lower() for s in L]
['hello', 'world', 'ibm', 'apple']


# IF...ELSE
>>> [x for x in range(1, 11) if x % 2 == 0]
[2, 4, 6, 8, 10]

>>> [x if x % 2 == 0 else -x for x in range(1, 11)]
[-1, 2, -3, 4, -5, 6, -7, 8, -9, 10]

```

### 生成器

[generator](https://www.liaoxuefeng.com/wiki/1016959663602400/1017318207388128)

> 列表生成式着实好用。但是存在内存限制(内存是有限的)

Example: 极端例子说如果创建100W个元素的列表。只访问极个别的内容。 其他的内存就浪费了。

```python
# 创建方式

>>> g = (x * x for x in range(10))
<generator object <genexpr> at 0x1022ef630>
# 遍历generator 需要用到For
for n in g:
    print(n)

next(g)
next(g)
next(g)
...
# 会报错。 
# StopIteration

#> 如果一个函数定义中包含 yield 关键字，那么这个函数就不再是一个普通函数，而是一个generator;
# 斐波那契数列. generator 方式
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield
        a, b = b, a + b
        n = n + 1
    return 'done'

g = fib(6)

# 通过For拿不到 generator 的Error
>>> g = fib(6)
>>> while True:
...     try:
...         x = next(g)
...         print('g:', x)
...     except StopIteration as e:
...         print('Generator return value:', e.value)
...         break
...
g: 1
g: 1
g: 2
g: 3
g: 5
g: 8
Generator return value: done


# 杨辉三角

def yhs(loop=6):
    n, r = 0, [1]
    while n < loop:
        yield r
        n = n + 1
        t = [0] + r + [0]
        r = [t[i] + t[i + 1] for i in range(len(t) - 1)]

```

### 迭代器

可以使用For的有 list、tuple、dist、set、str;

一类是集合数据类型，如list、tuple、dict、set、str等；

一类是generator，包括生成器和带yield的generator function。

这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

判断是否是迭代器
`from collections.abc import Iterator`

> 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator

```python

isinstance(obj, Iterator);

# 生成器都是 Iterator 对象
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数
>>> isinstance(iter([]), Iterator)
True
>>> isinstance(iter('abc'), Iterator)
True


```
凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

## 函数式编程

### 高阶函数
#### 函数当参数传入
#### map & reduce; func

```python 
map.  # 类似于Js中的 apply方法

# Example:

def f(x)
    return x * x

l = map(f, [1, 2, 3, 4, 5, 6...])


# reduce
from functools import reduce

def add(x, y):
    return x + y
l = reduce(add, [1, 2, 3, 4, 5])

def normalize(name):
    return str(name).lower().?capitalize()

def nomalize(name):
    return reduce(lambda x, y: x + y.lower(), name.upper())

    

```

#### lambda「匿名函数」

> 不需要像 def funcName 那样定义函数。 

`lambda x, y: x * 10 + y`

#### filter 高阶

> 过滤函数。 类似于js Array.filter()

**WARNNING:**注意到filter()函数返回的是一个`Iterator` 惰性序列 需要使用list(obj)转化


#### sorted「排序算法」

> 可以直接对list排序

```python 
sorted([1,2,23,3,4,45123,12,1])

# sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
>>> sorted([36, 5, -12, 9, -21], key=abs)
[5, 9, -12, -21, 36]

>>> sorted(['abs', 'bsf', 'cdsa', 'dfa', 'eag'], key=str.lower)

# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：

>>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
['Zoo', 'Credit', 'bob', 'about']



```

### 返回函数

> return 出去

返回函数。 会产生`闭包`
> 不会立马执行而是返回一个新的函数。 再执行就是结果

**WARNNING:** 闭包切记使用循环变量容易引起程序混乱。 

### 匿名函数

`lambda x, y: x * y`

### 装饰器「Decorator」

> 函数在Python中也是对象
func.__name__ 可以取到函数名称

```python

# HACK - 装饰器不是很理解、无法理解底层如何装饰

# 装饰器
def log(func):
    def wrapper(*args, **wk):
        print('call %s %s():', % (text, func.__name__))
        return func(*args, **wk)
    return wrapper

@log
def now():
    print('2020-02-22')

or

now = log(now)


# === === === ===

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')

or 

now = log('execute)(now)

# @functools.wraps(func)
# 改变函数wrapper对象的__name__的值。 变成用的函数的名称.

```

### 偏函数

> 自定义一个新的函数。 

```python
import functools

# 通过 functools.partial 函数制作。

int2 = functools.partial(int, base=2)
```
