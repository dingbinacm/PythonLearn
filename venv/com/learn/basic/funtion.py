import math
# max
print(max(1, 53, 4, 3))
# 数据类型转换
print(int("123"))
print(str(244))
print(float("434.5"))
# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = abs
print(a(-4))
# define function
# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type")
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-99))
"""
如果想定义一个什么事也不做的空函数，可以用pass语句：
def nop():
    pass
pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
pass还可以用在其他语句里，比如：
if age >= 18:
    pass
缺少了pass，代码运行就会有语法错误。
"""
age = 29
if age > 19:
    pass

# 返回多个值


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


t = move(100, 100, 60, math.pi / 6)
print(t[0], t[1])
"""
默认参数
一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
二是如何设置默认参数。
当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
"""
def pow(x, n=2):
    data = x
    while n > 1:
        data = data * x
        n = n - 1
    return data
print(pow(9,3))

def enroll(name, age=15, sex="man"):
    print("name",name)
    print("age",age)
    print("sex",sex)

enroll("dingbin", 53,"woman")
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017261630425888
# 可变参数
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1, 2, 3))
