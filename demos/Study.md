[toc]

# 小记

> python 是一门动态语言。

## py 类型

- 整数 int
  - 可以通过`_`去分割特别大的数字 100000 => 10_0000;
  - 十六进制也可以如此
- 浮点数 float
  - 可以用科学计数法表示`1.23e9`
- 字符串 string
  - 用单引号或双引号括包裹起来的任意文本内容
- 布尔值 Boolean - True&False
  - and、or、not 运算符。
- None 表示空值-非 0;特殊的空值
- list
- tuple
- dict
- set

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

`变量`
可变的量;

`常量`

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

> 与 C 语言相似

```python
>>> 'Hello, %s' % 'world'
'Hello, world'

>>> 'Hi, %s, you have $%d.' % ('Michael', 1000000)
'Hi, Michael, you have $1000000.'

```

| Placeholder | Desc         |
| :---------- | ------------ |
| %d          | 整数         |
| %s          | 字符串       |
| %f          | 浮点数       |
| %x          | 十六进制整数 |

> 如果你不太确定应该用什么，%s 永远起作用，它会把任何数据类型转换为字符串

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

> list 是一组*有序*的*集合*。 Js 中的数组

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

> dist 全称： dictionary 或其他语言中的 map 或对象
> 使用键值对

无序字典

dist:
查找和插入的速度极快，不会随着 key 的增加而变慢；
需要占用大量的内存，内存浪费多。

而 list 相反：
查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。

```python
dist[key] # 不存在会报错

可以通过 key in dist 判断
或 dist.get(key, defaultValue)

# delete

dist.pop(key)

```

> set 与 dist 类似也是 key&val 集合；但不能存储 val 由于 Key 的不重复性。所以在 set 中没有重复的 Key.

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
**_WARNNING: 命名关键词为 Python3 持有_**

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

> 通过 For 循环进行遍历。 俗称迭代

可迭代 list & tuple & dist & set

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

> 列表生成式即 List Comprehensions，是 Python 内置的非常简单却强大的可以用来创建 list 的生成式。

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

Example: 极端例子说如果创建 100W 个元素的列表。只访问极个别的内容。 其他的内存就浪费了。

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

可以使用 For 的有 list、tuple、dist、set、str;

一类是集合数据类型，如 list、tuple、dict、set、str 等；

一类是 generator，包括生成器和带 yield 的 generator function。

这些可以直接作用于 for 循环的对象统称为可迭代对象：Iterable。

判断是否是迭代器
`from collections.abc import Iterator`

`Iterator //惰性计算序列`

> 可以被 next()函数调用并不断返回下一个值的对象称为迭代器：Iterator

```python

isinstance(obj, Iterator);

# 生成器都是 Iterator 对象
# 把list、dict、str等Iterable变成Iterator可以使用iter()函数
>>> isinstance(iter([]), Iterator)
False
>>> isinstance(iter('abc'), Iterator)
False


```

凡是可作用于 for 循环的对象都是 Iterable 类型；

凡是可作用于 next()函数的对象都是 Iterator 类型，它们表示一个惰性计算的序列；

集合数据类型如 list、dict、str 等是 Iterable 但不是 Iterator，不过可以通过 iter()函数获得一个 Iterator 对象。

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

> 过滤函数。 类似于 js Array.filter()

**WARNNING:**注意到 filter()函数返回的是一个`Iterator` 惰性序列 需要使用 list(obj)转化

#### sorted「排序算法」

> 可以直接对 list 排序

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

> 函数在 Python 中也是对象
> func.**name** 可以取到函数名称

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
# 根据现有函数加工

int2 = functools.partial(int, base=2)

# > 当函数的参数个数太多，需要简化时，使用functools.partial 可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。
```

## 模块

> 在计算机程序的开发过程中，随着程序代码越写越多，在一个文件里代码就会越来越长，越来越不容易维护。  
> 为了编写可维护的代码，我们把很多函数分组，分别放到不同的文件里，这样，每个文件包含的代码就相对较少，很多编程语言都采用这种组织代码的方式。在 Python 中，一个.py 文件就称之为一个模块（Module）。

**WARNNING:**确保不会与内置函数名重复即可。

```python

mycompany   # package 包名称
├─ __init__.py # mycompany的主[int]模块
├─ abc.py   # 包里里面的abc模块
└─ xyz.py   # 包里里面的xyz模块

```

#### 安装模块

```python

# 查看当前python安装第三方模块的路径
# python 查看第三方目录会在已存在的目录中搜索。
import sys
sys.path

# 可以添加自己的第三方模块目录
sys.path.append('/path/path/path/path')
```

## 面向对象编程

> 面向对象编程——Object Oriented Programming，简称 OOP，是一种程序设计思想。OOP 把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。

```python

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('that %sm of score: %s' % (self.name, self.score))

stud1 = Student('menk', 99)

stud1.print_score()

# 可以添加属性名称与密码

stud1.name = 'deoc' # 可以自己手动添加属性名称;

# 在类中Class中。 所有的函数第一个参数都是self;实例自身

```
### 数据封装.

> `class`类中、自定义函数

### 访问限制。

> 在 Class 内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。

```python

# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问

class Student(Object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def __func(self):
        pass

# 以双划线开头的是隐私变量 private. 

# 以双划线开头  & 结尾的是特殊变量

```

### 继承 & 多态。

```python

# 继承

class Animal(object):
    
    def run():
        pass

# 多态（多种状态）
# 子类与基类共同存在某个方法时。 子类会覆盖基类的方法。 这就是多态

# 判断一个变量是否是某个类型可以用isinstance()判断：

>>> isinstance(a, list)
True


# 不用管原来的代码是如何调用的。这就是著名的“开闭”原则：
# 对扩展开放：允许新增Animal子类；
# 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。


# 这就是动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。

# Python的“file-like object“就是一种鸭子类型。对真正的文件对象，它有一个read()方法，返回其内容。但是，许多对象，只要有read()方法，都被视为“file-like object“。许多函数接收的参数就是“file-like object“，你不一定要传入真正的文件对象，完全可以传入任何实现了read()方法的对象。

# 小结
# 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。

# 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。

```

### 获取对象信息.

> ??? 当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？

```python

>>> type(123)
<class 'int'>

>>> type(None)
<type(None) 'NoneType'>

# 如果一个变量指向函数或者类，也可以用type()判断：

>>> type(abs)
<class 'builtin_function_or_method'>
>>> type(a)
<class '__main__.Animal'>


# change

# types 可以判断复杂引用类型。
# Example func 是否相同
import types

>>> type(func) == types.functionType
True

>>>type(abs) == types.BuiltinFunctionType # 是否是内置函数

>>> type(lambda x: x)==types.LambdaType # 是否是匿名函数

>>> type(g) == types.generatorType # 是否是高阶函数-生成器

# 关于对象的继承 isinstance();
# 判断Class是否是被继承的内容。
# 尽可能用isinstance()去判断对其类型“一网打尽”

# === ==== 

# dir() 可以获得内容的所有属性和方法. 
>>> dir('aa')
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']


# 类似__xxx__的属性和方法在Python中都是有特殊用途的
# 另外我们可以覆盖类中的原有函数

class Myobj():
    def __len__():
        return 100
    
h = Myobj()

>> len(h)
100


# 只获取还是对象的属性方法还是不够的。 还有可以获取、设置、判断是否存在
# getattr()\setattr()\hasattr()

getattr(obj实例, key, defaultValue) # 可以获取属性Key. 如果不存在可以取值defaultValue
# 不然会报错。 AttributeError.


setattr(obj实例, key, Val)

hasattr(objStance, key)
```

### 实例属性 & 类属性

> ? 实例属性与类属性如果存在属性名称相同值不同就会存在未知的错误❌。 禁止使类属性名称与实例属性名称相同的Name.

* 实例属性属于各个实例所有，互不打扰
* 类属性属于类所有, 所有实例共享同一属性
* 不要对实例属性和类属性使用相同的名称否则将产生***难以发现***的错误


## 面向对象高级编程

> 数据封装、继承和多态只是面向对象程序设计中最基础的3个概念。

> === 我们会讨论多重继承、定制类、元类等概念。

### __slots__

*给实例定义一个方法*

```python

class S():
    pass

def set_age(self, age):
    self.age = age

from types import MethodType

s = S()

s.set_age = MethodType(set_age, s) # 给实例绑定一个方法

```

***WARNNING tips:*** 对一个实例绑定方法;对其他实例不产生影响与变化。
可以对Class类进行绑定属性与方法、这样所有的实例对象都会存在类中存在的属性和方法;


*如果这个时候我们想限制实例属性注入的属性名称与方法。可以通过__solts__去设置*

```python

class Abc():
    __slots__ = ('name', 'age') # 通过tuple定义允许绑定的属性名称。

a = Abc()

a.name = 'marks'

>>> a.score = 99

AttributeError: 'Student' object has no attribute 'score'.

# 错误绑定会收错误。 AttributeError

```

***WARNNING Tips:*** 定义`__slots__`仅对当前类实例有效果、对继承子类不起作用。
除非在子类中也定义`__slots__`，这样，子类实例允许定义的属性就是自身的`__slots__`加上父类的`__slots__`

### @property

> 属性名称禁止被实例随意赋值修改内容。可以通过`@property`装饰器去约定该内容

```python

class Student(object):

    @property # 这样设置过后该方法可以通过属性名的方式调用  student.score
    def score(self):
        return self.score or 0
    
    @score.setter # 设置装饰器 score的设置方法。 score.setter
    def score(self, val):
        self.score = val
    
    # 定义只读属性就是只定义属性不去定义设置方法就是制度属性

```

### 多重继承

> 多重继承及多次继承、继承多次内容等。

#### MixIn

> 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。

> MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系

```python

class Animal(object):
    pass

class RouMixin(Animal):
    pass

class Dog(Animal, RouMixin):
    pass

```

### 定制类

[click into info](https://www.liaoxuefeng.com/wiki/1016959663602400/1017590712115904)

> 已知`__slots__`、`__str__`、`__len__`在类中具有特殊意义

```python

>>> print(Student('Michael'))
<__main__.Student object at 0x109afb190> # 默认打印内存地址


class Student(object):
    __slots__ = ('name', 'age', 'sex')

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name

>>> print(Student('Michael'))
Student object (name: Michael) # 通过类中`__str__`可以定制输出内容


# 这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
# 解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法

...
def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__ # 让函数__repr__与__str__相同。
...

# ===  __iter__
# > 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。


# Example:
# 斐波那契数列为例，写一个Fib类，可以作用于for循环
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

>>> for n in Fib():
...     print(n)
...
1
1
2
3
5
...
46368
75025

# === __getitem__
# > Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：

class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

>>> f = Fib()
>>> f[0]
1
>>> f[1]
1
>>> f[2]
2
>>> f[3]
3
>>> f[10]
89
>>> f[100]
573147844013817084101

但是list有个神奇的切片方法：
>>> list(range(100))[5:10]
[5, 6, 7, 8, 9]
对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：

class Fib(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

# === 与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。

# === __getattr__
> 可以用这个方法定义返回内容。 假设不存在该属性方法可以直接放回None.

def __getattr__(self, attr):
        if attr=='score':
            return 99

# 可以定义抛出错误、抛出属性错误

 def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)

# === __call__
# > 类似于调用自身实例对象

class Abc(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

a = Abc('aaa')

a() # print => xxx


# ？？？？？ 怎么判断一个变量是对象还是函数呢？
# 能被调用的对象就是一个Callable对象
>>> callable(Student())
True
>>> callable(max)
True
>>> callable([1, 2, 3])
False
>>> callable(None)
False
>>> callable('str')
False

# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象


```

### 使用枚举类

> 定义不可变枚举采用类的方式

```python

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

# === 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：
form enum import Enum, unique

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

>>> Weekday['Sun'] # Weekday.Sun
>>> Weekday['Sun'].value # 0

```

### 使用元类


```python 

# type()
# type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello。
>>> class Abc(object):
...     pass
...
>>> type(1)
<type 'int'>
>>> type(Abc)
<type 'type'>
>>> a = Abc()
>>> type(a)
<class '__main__.Abc'>

# 我们可以通过type()函数创建出Hello类
>>> def fn(self, name='w'):
...     print('Hello, %s.' % name)
...
>>> Hello = type('Hello', (object,), dict(hello=fn))
>>> h=Hello()
>>> h.hello()
Hello, w.
>>> type(Hello)
<type 'type'>
>>> type(h)
<class '__main__.Hello'>

# 要创建一个class对象，type()函数依次传入3个参数：
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

# === metaclass
# LINK -- https://www.liaoxuefeng.com/wiki/1016959663602400/1017592449371072
# metaclass，直译为元类，
# 除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。

# 定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：

# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list, metaclass=ListMetaclass):
    pass

# 当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。

# __new__()方法接收到的参数依次是：
# 当前准备创建的类的对象；
# 类的名字；
# 类继承的父类集合；
# 类的方法集合。

```



## 错误、调试和测试

> 在程序运行中总是会遇到各种各样的错误。

> python 中存在内置的异常处理机制

#### 错误处理

> 约定错误返回码代表错误(-1)


> 故而高级语言中存在一套try...except...finally...的错误处理机制

```python 

try:
    r = 10 / 0
    print(r)
except ZeroDivisionError as e:
    print('except', e)
finally:
    print('The end.')

# 不同类型错误很多。 

ValueError
ZeroDivisionError
...

# 此外，如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：

try:
    # ...
except ValueError as e:
    # ...
else:
    print('xxxx')
finally:
    print('end')
```

>  Python的错误其实也是class，所有的错误类型都继承自BaseException，所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。比如：

```py
try:
    foo()
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')

# 第二个except永远也捕获不到UnicodeError，因为UnicodeError是ValueError的子类，如果有，也被第一个except给捕获了。

# Python所有的错误都是从BaseException类派生的，常见的错误类型和继承关系看这里：

# https://docs.python.org/3/library/exceptions.html#exception-hierarchy
```

##### 调用栈

> 如果错误没有被捕获，它就会一直往上抛，最后被Python解释器捕获，打印一个错误信息，然后程序退出。

> ? 寻找错误的源头。 才能正确解析错误内容

##### 记录错误

> 如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，但程序也被结束了。既然我们能捕获错误，就可以把错误堆栈打印出来，然后分析错误原因，同时，让程序继续执行下去。

> Python内置的logging模块可以非常容易地记录错误信息：

```py
# err_logging.py

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')


# !perform
$ python3 err_logging.py
ERROR:root:division by zero
Traceback (most recent call last):
  File "err_logging.py", line 13, in main
    bar('0')
  File "err_logging.py", line 9, in bar
    return foo(s) * 2
  File "err_logging.py", line 6, in foo
    return 10 / int(s)
ZeroDivisionError: division by zero
END
```

##### 抛出错误

> 因为错误是class，捕获一个错误就是捕获到该class的一个实例。因此，错误并不是凭空产生的，而是有意创建并抛出的。Python的内置函数会抛出很多类型的错误，我们自己编写的函数也可以抛出错误。

> 如果要抛出错误，首先根据需要，可以定义一个错误的class，选择好继承关系，然后，用raise语句抛出一个错误的实例：

```py
def foo(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo('0')

# perform
$ python3 err_raise.py 
Traceback (most recent call last):
  File "err_throw.py", line 11, in <module>
    foo('0')
  File "err_throw.py", line 8, in foo
    raise FooError('invalid value: %s' % s)
__main__.FooError: invalid value: 0


raise 可以抛出自定义错误类型

如果py内置错误提示满足、尽可能采用内置错误表达式

# *Tips
在except错误代码段中继续通过 raise抛出错误、可以改变错误类型；
But. 决不应该把一个IOError转换成毫不相干的ValueError。

```

##### 测试

> 调试Bugs 如何做

* 通过print打印错误
* 断言?(assert)代替print
* logging
* pdb
* IDE


```py
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main():
    foo('0')

# 如果断言失败，assert语句本身就会抛出AssertionError：
$ python err.py
Traceback (most recent call last):
...
AssertionError: n is zero!

# 程序中如果到处充斥着assert，和print()相比也好不到哪去。不过，启动Python解释器时可以用-O参数来关闭assert：

$ python -o x.py
```

```py
import logging
logging.basicConfig(level=logging.INFO)

# 这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。

# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

```


```py
# 第4种方式是启动Python的调试器pdb，让程序以单步方式运行，可以随时查看运行状态。我们先准备好程序：

# err.py
s = '0'
n = int(s)
print(10 / n)


$ python -m pdb err.py
> /Users/michael/Github/learn-python3/samples/debug/err.py(2)<module>()
-> s = '0'

# 以参数-m pdb启动后，pdb定位到下一步要执行的代码-> s = '0'。输入命令l来查看代码：

(Pdb) l
  1     # err.py
  2  -> s = '0'
  3     n = int(s)
  4     print(10 / n)

# 输入命令n可以单步执行代码

(Pdb) n
> /Users/michael/Github/learn-python3/samples/debug/err.py(3)<module>()
-> n = int(s)
(Pdb) n
> /Users/michael/Github/learn-python3/samples/debug/err.py(4)<module>()
-> print(10 / n)

# 任何时候都可以输入命令p 变量名来查看变量：

(Pdb) p s
'0'
(Pdb) p n
0
# 输入命令q结束调试，退出程序：
(Pdb) q

# 这种通过pdb在命令行调试的方法理论上是万能的，但实在是太麻烦了，如果有一千行代码，要运行到第999行得敲多少命令啊。还好，我们还有另一种调试方法。

# pdb.set_trace()

# 这个方法也是用pdb，但是不需要单步执行，我们只需要import pdb，然后，在可能出错的地方放一个pdb.set_trace()，就可以设置一个断点

# err.py
import pdb

s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)

# 运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，可以用命令p查看变量，或者用命令c继续运行：

$ python err.py 
> /Users/michael/Github/learn-python3/samples/debug/err.py(7)<module>()
-> print(10 / n)
(Pdb) p n
0
(Pdb) c
Traceback (most recent call last):
  File "err.py", line 7, in <module>
    print(10 / n)
ZeroDivisionError: division by zero


```

### 单元测试

> 如果你听说过“测试驱动开发”（TDD：Test-Driven Development），单元测试就不陌生。                
> 单元测试是用来对一个模块、一个函数或者一个类来进行正确性检验的测试工作。

```py

# 自定义类。
# mydict.py
class Dict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)
    
    def __getatter__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute %s" % key)
    
    def __setattr__(self, key, val):
        self[key] = val

```


> py自带的unittest单元测试模块

```py
# mydict_test.py

import unittest

form mydict import Dict

class TestDict(unittest.TestCase):
    
    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1) # assertEqual 断言相等
        self.assertEqual(d.b, 'test')
        self.assertTrue(isinstance(d, dict)) # 断言True
    
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')
    
    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')
    
    # 断言抛出KeyError
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']
    
    # 断言抛出AttributeError
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty


# 运行单元测试

# 命令行运行mydict_test.py
if __name__ == '__main__':
    unittest.main()

# or

$ python -m unittest mydict_test
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK


# ==== 

# setUp与tearDown
# > 可以在单元测试中编写两个特殊的setUp()和tearDown()方法。这两个方法会分别在每调用一个测试方法的前后分别被执行。

class TestDict(unittest.TestCase):

    def setUp(self):
        print('setUp...')

    # ... more func


    def tearDown(self):
        print('tearDown...')



# EXAMPLE ========================
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score >= 80 and self.score <= 100: 
            return 'A'
        elif self.score >= 60 and self.score <= 79:
            return 'B'
        elif self.score < 60 and self.score >= 0:
            return 'C'
        else:
            raise ValueError

class TestStudent(unittest.TestCase):

    def test_80_to_100(self):
        s1 = Student('Bart', 80)
        s2 = Student('Lisa', 100)
        self.assertEqual(s1.get_grade(), 'A')
        self.assertEqual(s2.get_grade(), 'A')

    def test_60_to_80(self):
        s1 = Student('Bart', 60)
        s2 = Student('Lisa', 79)
        self.assertEqual(s1.get_grade(), 'B')
        self.assertEqual(s2.get_grade(), 'B')

    def test_0_to_60(self):
        s1 = Student('Bart', 0)
        s2 = Student('Lisa', 59)
        self.assertEqual(s1.get_grade(), 'C')
        self.assertEqual(s2.get_grade(), 'C')

    def test_invalid(self):
        s1 = Student('Bart', -1)
        s2 = Student('Lisa', 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()

if __name__ == '__main__':
    unittest.main()

```

### 文档测试

> 文档测试也很有用。 比单元测试更便捷些许。

[click to View。不懂看文档](https://www.liaoxuefeng.com/wiki/1016959663602400/1017605739507840)

```py
import doctest # 文档测试

```

> ???Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试。

```py
import re

>>> m = re.search('(?<=abc)def', 'abcdef')
>>> m.group(0)
def

# 多行注释
'''
这是注释内容这是注释内容这是注释内容这是注释内容。。。
这是注释内容。。
这是注释内容。。
...
'''

# mydict2.py
class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__=='__main__':
    import doctest
    doctest.testmod()

```