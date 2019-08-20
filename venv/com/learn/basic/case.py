#!/usr/bin/python3
# 条件判断
age = 3
if age > 18:
    print("adult")
elif age >= 6:
    print("teenager")
else:
    print("kid")
# input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成这件事情：
birth = input("birth: ")
birth = int(birth)
if birth < 2000:
    print("00 qian")
else:
    print("00 hou")

