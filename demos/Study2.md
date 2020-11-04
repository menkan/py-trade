# continue

## IO编程

> IO在计算机中称为Input/Output.也就是输入和输出。由于程序和运行时数据是在内存中驻留，由CPU这个超快的计算核心来执行，涉及到数据交换的地方，通常是磁盘、网络等，就需要IO接口。

[IO Desc](https://www.liaoxuefeng.com/wiki/1016959663602400/1017606916795776)

*Steam(流)*

存在**同步**与**异步**两种方式

### 文件读写

* read file
```py
>>> file = open('/User/xxx/xx.py', 'r')

# 不存在的展示方式
>>> f=open('/Users/michael/notfound.txt', 'r')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '/Users/michael/notfound.txt'

file.read() # 可以读取全部内容
file.close() # 变比打开的文件

# 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：

try:
  f = open('/path/to/file', 'r')
  print(f.read())
finally:
  if f:
    f.close()

# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：

with open('/path/to/file', 'r') as f:
  print(f.read())

f.read() # 一次性提取全部
f.read(size) # 提取部分错误
f.readline() # 提取一行
f.readlines() # 一行一行提取;全部提取出来通过List方式存储

# readlines 多行For遍历
for line in f.readlines():
  print(line.strip()) # 把末尾的'\n'删掉

# === file-like Object

# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。

# StringIO就是在内存中创建的file-like Object，常用作临时缓冲。

# === 二进制文件 
# 前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：

>>> f = open('/Users/michael/test.jpg', 'rb')
>>> f.read()
b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # 十六进制表示的字节

# 字符编码
# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：

>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
>>> f.read()
'测试'

# ?error?
# UnicodeDecodeError # 如存在非法字符。
# 遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：

# errors='ignore' # 忽略错误ShowTime.
>>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')




# ==== write files
# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：

>>> f = open('/Users/michael/test.txt', 'w')
>>> f.write('Hello, world!')
>>> f.close()

# 你可以反复调用write()来写入文件，但是务必要调用f.close()来关闭文件。当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险

with open('/Users/michael/test.txt', 'w') as f:
  f.write('Hello, world!')

# 要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动转换成指定编码。
如果通过 w写入文件会覆盖内容
需要通过 a追加文件

```

### StringIO and BytesIO

[click to view](https://www.liaoxuefeng.com/wiki/1016959663602400/1017609424203904)

StringIo 算是内存Io
StringIO顾名思义就是在内存中读写str。

```py
from io import StringIO

f = StringIO() # 实例f内存IO对象

>>> f.write('hello')
5

>>> f.write(' ')
1

>>> f.write('world!')
6

>>> print(f.getvalue()) # f.getvalue() 获取f实例内存中全部数据;
hello world!

# --- string.strip() # 获取本行内容去掉换行符好

>>> from io import StringIO
>>> f = StringIO('Hello!\nHi!\nGoodbye!')
>>> while True:
...     s = f.readline()
...     if s == '':
...         break
...     print(s.strip())
...
Hello!
Hi!
Goodbye!

```

```py
# BytesIO
# 二进制数据，就需要使用BytesIO。
# BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：

>>> from io import BytesIO
>>> f = BytesIO()
>>> f.write('中文'.encode('utf-8')) # 写入的不是str 而是通过encode进行编码的bytesIo
6
>>> print(f.getvalue())
b'\xe4\xb8\xad\xe6\x96\x87'

# 和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：

>>> from io import BytesIO
>>> f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
>>> f.read()
b'\xe4\xb8\xad\xe6\x96\x87'

```

### 操作文件与目录
