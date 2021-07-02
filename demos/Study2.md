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

> 操作文件目录。 内置存在操作目录的模块与方法;

```py
import os # 操作文件目录内容.

>>> os.name # 操作系统名称
'posix'

# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。

>>> os.uname() # 输出详细信息。 Window不支持该函数。

# 环境变量
>>> os.environ
environ({'TERM_SESSION_ID': 'w0t0p0:1DFD9215-DE7C-41E2-8C5E-902B60E4833D', 'SSH_AUTH_SOCK': '/private/tmp/com.apple.launchd.dZn1tn6t9s/Listeners', 'LC_TERMINAL_VERSION': '3.3.12', 'COLORFGBG': '7;0', 'ITERM_PROFILE': 'Default', 'XPC_FLAGS': '0x0', 'PWD': '/Users/xutongze/Documents/menkan/py-trade', 'SHELL': '/bin/zsh', 'SECURITYSESSIONID': '186c8', 'LC_CTYPE': 'UTF-8', 'TERM_PROGRAM_VERSION': '3.3.12', 'TERM_PROGRAM': 'iTerm.app', 'PATH': '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Library/Apple/usr/bin', 'LC_TERMINAL': 'iTerm2', 'COLORTERM': 'truecolor', 'TERM': 'xterm-256color', 'HOME': '/Users/xutongze', 'TMPDIR': '/var/folders/c1/28qsr99x3dzcwty9bs39k68h0000gn/T/', 'USER': 'xutongze', 'XPC_SERVICE_NAME': '0', 'LOGNAME': 'xutongze', 'LaunchInstanceID': 'CA1D5A77-84A3-40D8-ACFE-EBA382781300', 'ITERM_SESSION_ID': 'w0t0p0:1DFD9215-DE7C-41E2-8C5E-902B60E4833D', '__CF_USER_TEXT_ENCODING': '0x1F5:0x0:0x0', 'SHLVL': '1', 'OLDPWD': '/Users/xutongze/Documents/menkan', 'ZSH': '/Users/xutongze/.oh-my-zsh', 'PAGER': 'less', 'LESS': '-R', 'LSCOLORS': 'Gxfxcxdxbxegedabagacad', '_': '/usr/local/bin/python3', '__PYVENV_LAUNCHER__': '/usr/local/bin/python3'})

# 获取具体某个环境变量的值 `os.environ.get(key)`获取
>>> os.environ.get('PATH')
'/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/X11/bin:/usr/local/mysql/bin'
>>> os.environ.get('x', 'default') # 没有的话获取第二个key默认值。
'default'

# 操作文件和目录
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：

# 当前地址位置
>>> os.path.abspath('.')
'/Users/xutongze/Documents/menkan/py-trade'

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
>>> os.path.join('/Users/michael', 'testdir')
'/Users/michael/testdir'

# 然后创建一个目录:
>>> os.mkdir('/Users/michael/testdir')

# 删掉一个目录:
>>> os.rmdir('/Users/michael/testdir')

# === 因为Win&Mac路径展示方式不同。 路径合并的话最好通过 `os.path.join(xx, xx, xx)`去合并

# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
>>> os.path.split('/Users/michael/testdir/file.txt')
('/Users/michael/testdir', 'file.txt')

# `os.path.splitext()` 可以直接让你得到文件扩展名，很多时候非常方便：
>>> os.path.splitext('/path/to/file.txt')
('/path/to/file', '.txt')


# rename
>>> os.rename(oldname, newname)
# 删掉文件:
>>> os.remove('test.py')

# os中没有提供Copy文件等功能。
# === shutil模块中提供了该函数 `copyfile()`


# 最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：
>>> [x for x in os.listdir('.') if os.path.isdir(x)]
['.lein', '.local', '.m2', '.npm', '.ssh', '.Trash', '.vim', 'Applications', 'Desktop', ...]

# 列出所有.py 文件
>>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
['apis.py', 'config.py', 'models.py', 'pymonitor.py', 'test_db.py', 'urls.py', 'wsgiapp.py']

```

### 序列化

> 在程序运行的过程中，所有的变量都是在内存中; 一旦运行结束就会收回内存变量

> 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思

> 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上

> 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

> PY中提供了内置的序列化模块`pickle`

```py
# EXAMPLE:

import pickle

>>> d = dict(name='Bob', age=20, score=88)
>>> pickle.dumps(d) # 序列化就是把数据格式化bytes然后存储到内存\磁盘中
b'\x80\x03}q\x00(X\x03\x00\x00\x00ageq\x01K\x14X\x05\x00\x00\x00scoreq\x02KXX\x04\x00\x00\x00nameq\x03X\x03\x00\x00\x00Bobq\x04u.'

>>> f = open('/xxx/xx.py', 'wb')
>>> pickle.dump(d, f) # 把数据格式化成 file-like Object 
>>> f.close()
```

#### JSON

> js and py 相差不大转换轻松

```py

import json

d = dict(name='mk', age=20)
>>> json.dumps(d) # 转换成JSON格式数据
'{"age": 20, "score": 88, "name": "Bob"}'
dump()方法可以直接把JSON写入一个file-like Object。

>>> json.loads(d) # 转换为py的dict格式数据
# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：

# JSON 进阶

# 搞定Class类实例 => json 化


#LINK  https://www.liaoxuefeng.com/wiki/1016959663602400/1017624706151424

```

## 进程与线程

> 对于操作系统来说，一个任务就是一个进程（Process）

> 同一个进程存在多个子任务(线程); 每个进程至少有一个线程


```py
# 多任务执行如何方法？
1.多进程方法
2.多线程方法
3.多进程多线程

同时执行多个任务通常各个任务之间并不是没有关联的，而是需要相互通信和协调，有时，任务1必须暂停等待任务2完成后才能继续执行，有时，任务3和任务4又不能同时执行，所以，多进程和多线程的程序的复杂度要远远高于我们前面写的单进程单线程的程序。
因为复杂度高，调试困难
```

#### 多进程（multiprocessing）

[click views](https://www.liaoxuefeng.com/wiki/1016959663602400/1017628290184064)


> unix/linux 提供了fork() 系统调用;fork()调用一次，返回两次，因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。

> 子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，所以，父进程要记下每个子进程的ID，而子进程只需要调用`getppid()`就可以拿到父进程的ID。

```py
import os
from multiprocessing import Process # process module of Windows .

```

###### Pool

> 进程池。 如果存在大量的子进程 可以通过进程池的方式批量创建子进程

#### 子进程(subprocesses)

```py
import subprocess # subprocesses modules.

```

## 正则表达式

> re modules in python;

```py
import re

re = r'ABC\-001'

re.match(r'\d[3]\-\d{3,8}$', '010-12345')

# match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None


# 切分字符串
>>> re.split(r'\s+', 'a b   c')
['a', 'b', 'c']
>>> re.split(r'[\s\,]+', 'a,b, c  d')
['a', 'b', 'c', 'd']
>>> re.split(r'[\s\,\;]+', 'a,b;; c  d')
['a', 'b', 'c', 'd']

# 分组
# ^(\d{3})-(\d{3,8})$分别定义了两个组，可以直接从匹配的字符串中提取出区号和本地号码：
>>> m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
>>> m
<_sre.SRE_Match object; span=(0, 9), match='010-12345'>
>>> m.group(0)
'010-12345'
>>> m.group(1)
'010'
>>> m.group(2)
'12345'

>>> t = '19:05:30'
>>> m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
>>> m.groups()
('19', '05', '30')


# 贪婪匹配

# 由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了。

# 必须让\d+采用非贪婪匹配（也就是尽可能少匹配），才能把后面的0匹配出来，加个?就可以让\d+采用非贪婪匹配：

>>> re.match(r'^(\d+?)(0*)$', '102300').groups()
('1023', '00')

# 编译
# 当我们在Python中使用正则表达式时，re模块内部会干两件事情：

# 编译正则表达式，如果正则表达式的字符串本身不合法，会报错；

# 用编译后的正则表达式去匹配字符串。

# 如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：

>>> import re
# 编译:
>>> re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
# 使用：
>>> re_telephone.match('010-12345').groups()
('010', '12345')
>>> re_telephone.match('010-8086').groups()
('010', '8086')
```

## 常用内建模块

### datetime

```py
# a datetime is modules in class is datetime
from datetime import datetime
now = datetime.now() # current time
print(now)

dt = datetime(2020, 4,18,12,20)

dt.timestamp() # 把时间转换成时间戳.

datetime.fromtimestamp(123124124) # 时间戳转换成datetime

# str => datetime
datetime.strptime('2020-9-2 18:19:59', '%Y-%m-%d %H:%M:%S')

# datetime转换为str
now = datetime.now()
now.strftime('%a, %b %d %H:%M')

# datetime加减
from datetime import datetime, timedelta

now = datetime.now()

now + timedelta(hours=10) # 当前时间加上 10个小时

# 本地时间转换为UTC时间
# 本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。
本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。

一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区：

>>> from datetime import datetime, timedelta, timezone
>>> tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
>>> now = datetime.now()
>>> now
datetime.datetime(2015, 5, 18, 17, 2, 10, 871012)
>>> dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00
>>> dt
datetime.datetime(2015, 5, 18, 17, 2, 10, 871012, tzinfo=datetime.timezone(datetime.timedelta(0, 28800)))
如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区。

# 时区转换
# utcnow()拿到当前的UTC时间，再转换为任意时区的时间

# 拿到UTC时间，并强制设置时区为UTC+0:00:
>>> utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
>>> print(utc_dt)
2015-05-18 09:05:12.377316+00:00
# astimezone()将转换时区为北京时间:
>>> bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
>>> print(bj_dt)
2015-05-18 17:05:12.377316+08:00
# astimezone()将转换时区为东京时间:
>>> tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
>>> print(tokyo_dt)
2015-05-18 18:05:12.377316+09:00
# astimezone()将bj_dt转换时区为东京时间:
>>> tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
>>> print(tokyo_dt2)
2015-05-18 18:05:12.377316+09:00
时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。

利用带时区的datetime，通过astimezone()方法，可以转换到任意时区。

注：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如上述bj_dt到tokyo_dt的转换。

```

### collections

#### namedtuple

```py


```