# Python 核心数据类型
# -*- coding: utf-8 -*-

# Python 数字数据类型用于存储数值。
a1 = 9 / 3                  # 除法，得到一个浮点数
print(a1,type(a1))      

a2 = 10 // 3                # 除法，取整除 - 向下取接近商的整数
print(a2,type(a2))

a3 = 10 % 3                 # 取余
print(a3,type(a3))

a4 = 2 ** 8                 # 乘方
print(a4,type(a4))

#print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：
print('Hello ',end="")
print('Yuejin!')
print()

#Python中的字符串用单引号 ' 或双引号 " 括起来，同时使用反斜杠 \ 转义特殊字符。
str = 'CharlyYue'

print (str)          # 输出字符串
print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
print (str[0])       # 输出字符串第一个字符
print (str[2:5])     # 输出从第三个开始到第五个的字符
print (str[2:])      # 输出从第三个开始的后的所有字符
print (str * 2)      # 输出字符串两次，也可以写成 print (2 * str) 
print (str + "TEST") # 连接字符串
print()

#集合（set）是由一个或数个形态各异的大小整体组成的，构成集合的事物或对象称作元素或是成员。
#可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
sites = {'Google', 'Taobao', 'Yuejin', 'Facebook', 'Zhihu', 'Baidu'}

print(sites)   # 输出集合，重复的元素被自动去掉

# 成员测试
if 'Yuejin' in sites :
    print('Yuejin 在集合中')
else :
    print('Yuejin 不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)
print(b)
print(a - b)     # 集合a中包含而集合b中不包含的元素
print(a | b)     # 集合a或b中包含的所有元素
print(a & b)     # 集合a和b中都包含了的元素
print(a ^ b)     # 不同时包含于a和b的元素

c = {x for x in 'abracadabra' if x not in 'abc'}
print(c)
print()

'''
Python 字典（dictionary）是Python中另一个非常有用的内置数据类型。
列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。
字典是一种映射类型，字典用 { } 标识，它是一个无序的 键(key) : 值(value) 的集合。
键(key)必须使用不可变类型。
在同一个字典中，键(key)必须是唯一的。
'''

dict = {}
dict['one'] = "1 - 造化科技教程"
dict[2]     = "2 - 造化科技工具"

tinydict = {'name': 'charley','code':1, 'site': 'www.python.org'}

print(dict['one'])          # 输出键为 'one' 的值
print(dict[2])              # 输出键为 2 的值
print(tinydict)             # 输出完整的字典
print(tinydict.keys())      # 输出所有键
print(tinydict.values())    # 输出所有值
print()
