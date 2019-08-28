# 每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包
# 模块名不要和系统模块名冲突，最好先查看系统是否已存在该模块，检查方法是在Python交互环境执行import abc，若成功则说明系统存在此模块
# import 模块使用-----作用域
# 类似__xxx__这样的变量是特殊变量，可以被直接引用
# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用


def _private_get(name):
    return "Hello, %s" % name


def greeting(name):
    return _private_get(name)


print(greeting("dingbin"))
