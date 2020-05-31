# encoding: utf-8

# dist
# xdist = {
#     "name": "menkan",
#     "age": 23,
#     "sex": "man"
# }
# query xdist dist in phoneNumber , default:176...
# print('print Key:', xdist.get('phoneNumber', '176...'))
# print('keys', xdist.keys())
# print('keys', list(xdist.keys()))
# for key in list(xdist.keys()):
#     print('KEY: ', key)
# print('vals', xdist.values())
# print('BOOLEAN:', 'phonenumber' in xdist)
# xdist.setdefault('xxx', 444)
# print(xdist['xxx'])
# print(xdist)
# try:
#     # print(xdist['xxx'])
#     print(xdist)
# except KeyError as e:
#     print('Key', e, 'not existent')
# else:
#     print('all goods?')
# finally:
#     print('allowed perform')


# set
# 存储内容不相同的元素

empty_set = set()
filter_set = {1, 2, 3}

# print(empty_set)
empty_set = {3, 4, 5}
# print(empty_set)
# empty_set.add(6)
# print(empty_set)
# print(type(filter_set))

empty_set.add(5)

# 交际、两个set都有的内容 ？ & ？
# 并集 任意一个有  ？ | ？
# 计算差集 ？ - ？
# 对称差集 ? ^ ?
# print(empty_set - filter_set)


class Human:
    name = 'menkan'

    def __init__(self):
        self.space = 'menkan'

    def say(self):
        print(self.name)
        pass

    # 表示类函数。 Class.method...
    @classmethod
    def eat(cls):
        print('eat semothing', cls)

    @staticmethod
    # 静态函数属性
    def run():
        print('runs...')

    @property
    # property注解，类似于get，set方法
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    @age.deleter
    def age(self):
        del self._age


# if __name__ == '__main__':
#     per = Human('menkan')
#
#     per.say() # print semoting

# subClass

class SubHuman(Human):
    def __init__(self, name, pawoder=['xxx', 'ccc']):
        self.pawoder = pawoder
        super.__init__(name)

    # reset father event -> say
    def say(self):
        print('sub class say event')

    def subSay(self):
        print('only sub class evetn subSay()')

if __name__ == '__main__':

    sup = SubHuman(name="Tick")

    if isinstance(sup, Human):
        print('yes, i|m human')

    if type(sup) is SubHuman:
        print('i am SUBHUMAN')

    # 查看方法查询的顺序
    # 先是自身，然后沿着继承顺序往上，最后到object
    print(Superhero.__mro__)  # => (<class '__main__.Superhero'>,
    # => <class 'human.Human'>, <class 'object'>)

# 生成器
# https://mp.weixin.qq.com/s?__biz=MzUyMTM5OTM2NA==&mid=2247484777&idx=1&sn=236b215aff90bf4cccb56b8385eece18&chksm=f9daf842cead7154ad10951904789ff549611e86df4fefae71653c7c96be627bee447dfc7f89&scene=21#wechat_redirect
# 装饰器
# https://mp.weixin.qq.com/s?__biz=MzUyMTM5OTM2NA==&mid=2247485152&idx=1&sn=1386f218b0d5674547599cf00befd93d&chksm=f9dafbcbcead72dd4329068c609c2becc9326be8d3f4b53f0193185747e778f6dbc805601fbe&scene=21#wechat_redirect

