from collections import Iterable
# 切片 取一个list或tuple的部分元素是非常常见的操作
L = ["Michael", "Sarah", "Tracy"]
r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)

print(L[0:3])
print(L[1:3])
print(L[-3:])

L = list(range(100))
print(L[10:20])
# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
T = (0, 1, 2, 3, 4, 5)
print(T[0:3])
# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
"""
在Python中，迭代是通过for ... in来完成的
list, tupple, dict, string 都可以迭代
只要作用于一个可迭代对象，for循环就可以正常运行
如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
"""
print(isinstance(123, Iterable))
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = []
for x in L1:
    if (isinstance(x, str)):
        L2.append(x.lower())
    else:
        continue
print(L2)
# 生成器 一种方式是,只要把一个列表生成式的[]改成()，就创建了一个generator
g = (x * x for x in range(4))
for n in g:
    print(n)
"""
你可能会问，为什么list、dict、str等数据类型不是Iterator？
这是因为Python的Iterator对象表示的是一个数据流，Iterator对象可以被next()函数调用并不断返回下一个数据，直到没有数据时抛出StopIteration错误。
可以把这个数据流看做是一个有序序列，但我们却不能提前知道序列的长度，只能不断通过next()函数实现按需计算下一个数据，所以Iterator的计算是惰性的，只有在需要返回下一个数据时它才会计算。
Iterator甚至可以表示一个无限大的数据流，例如全体自然数。而使用list是永远不可能存储全体自然数的。
凡是可作用于for循环的对象都是Iterable类型；
凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
Python的for循环本质上就是通过不断调用next()函数实现的，例如：
for x in [1, 2, 3, 4, 5]:
    pass
实际上完全等价于：

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
"""
