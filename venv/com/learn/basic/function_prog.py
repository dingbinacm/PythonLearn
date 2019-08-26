import functools, time
# 匿名函数
"""
def f(x):
    return x * x
关键字lambda表示匿名函数，冒号前面的x表示函数参数。
匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
"""
f = lambda x: x * x
print(f(5))


def is_odd(n):
    return n % 2 == 1


L = list(filter(lambda n: n % 2 == 1, range(1, 20)))
print(L)


# 装饰器


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print("call %s():")
        return func(*args, **kw)
    return wrapper


@log
def now():
    print("2019-8-26")


now()

# 得到函数的执行时间
def funtion_wrapper(func):
    def wrapper(*args, **kw):
        print("start it")
        fun = func(*args, **kw)
        print("end it")
        return fun
    return wrapper


@funtion_wrapper
def metric(fn):
    print('%s executed in %s ms')
    return fn


metric(5)
# 偏函数
print(int("12345"))
print(int("12345", base=8))
