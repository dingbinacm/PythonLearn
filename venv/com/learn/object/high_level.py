# 正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：


class Student(object):
    pass


s = Student()
s.name = "dingbin"

print(s.name)

# 还可以尝试给实例绑定一个方法：
# 但是，给一个实例绑定的方法，对另一个实例是不起作用的
"""
但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
"""


class Student(object):
    __slots__ = ("name", "age")


s = Student()
# s.score = 100

# print(s.score)
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__


class GradusteStudent(Student):
    pass


g = GradusteStudent()
g.score = 100
# 多重继承
"""
由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。
只允许单一继承的语言（如Java）不能使用MixIn的设计
"""
# 大类:


class Animal(object):
    pass


class Mammal(Animal):
    pass


class Runnable(object):
    def run(self):
        print('Running...')


class Flyable(object):
    def fly(self):
        print('Flying...')


class Dog(Mammal, Flyable):
    pass


dog = Dog()
dog.fly()
# 当我们需要定义常量时，一个办法是用大写变量通过整数来定义，例如月份：
