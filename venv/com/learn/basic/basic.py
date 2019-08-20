#!/usr/bin/python3
print(0x10)
print("I am ok")
print(True and False)
print(True or False)
print(not True)
# 特殊的值，空值
print(None)
a = 123
print(a)
a = True
print(a)
a = 'abc'
print(a)
b = a
a = 'ddd'
print(b)
# 在Python中，通常用全部大写的变量名表示常量
PI = 3.141592653
# / 精确除法， // 地板除法， %
print(4//3)
print("hello", "world")
# '' ""都可以表示字符串
print("hello", "\"workld\"")
"""
在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。

用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件：
rw-file-utf-8

浏览网页的时候，服务器会把动态生成的Unicode内容转换为UTF-8再传输到浏览器：
"""
# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
print(ord("a"))
print(chr(102))
print("你好".encode("utf-8"))
# %运算符就是用来格式化字符串的， 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：
print("hi, %s, you have $%d" % ("dingbin", 90000))
# 当str和bytes互相转换时，需要指定编码。最常用的编码是UTF-8

# list, trup
# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ["MIahael", "Bob", "Tracy"]
print(classmates)
# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
classmates.append("risken")
print(classmates[-1])
print(classmates)
classmates.insert(1, "disk")
print(classmates)
# 要删除末尾的元素，可以用pop
classmates.pop()
print(classmates)
# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
classmates.pop(0)
print(classmates)
classmates[0] = "mike"
print(classmates)
# list里面的元素的数据类型也可以不同，比如：
L = ["Apple", 124, True]
print(L)
# list元素也可以是另一个list，比如：,多唯数组
p = ["asp", "php"]
s = ["python", "java", p, "scheme"]
print(s[2][1])
# tupple 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：
# 不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
classmates = ("michale", "Bob")
print(classmates)
t = (1,)
# tuple所谓的“不变”是说，tuple的每个元素，指向永远不变
t = ("a", "b",["c", "d"])
t[2][1] = "dis"
print(t)

