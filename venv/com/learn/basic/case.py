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

# 循环
names = ["Michael", "Bob", "Tracy"]
for name in names:
    print(name)
# range(5)生成的序列是从0开始小于5的整数：
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
# while
sum = 0
n = 100
while n > 0:
    sum = sum + n
    n = n - 1
    if n % 2 == 0:
        continue
    if n < 3:
        break
print(sum)


