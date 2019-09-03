import logging
logging.basicConfig(level=logging.INFO)
# 错误处理
# try catch finally
# https://docs.python.org/3/library/exceptions.html#exception-hierarchy    常见的错误类型和继承关系看这里


def bar(s):
    return 10 / int(s)


def main():
    try:
        bar("0")
    except Exception as e:
        logging.exception(e)
        pass
    except ValueError as e:
        pass
    finally:
        print("finally")


# main()
# 抛出错误


class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError("invalid value %s " % s)
    return 10 / n


# foo("0")
# 调试
"""
logging
把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件：
"""
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
