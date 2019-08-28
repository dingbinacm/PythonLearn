"""
Python中，定义类是通过class关键字：class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，
表示该类是从哪个类继承下来的，继承的概念我们后面再讲，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类

可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去
注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去
"""
# 类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。
# 实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问


class Student(object):
    name_id = 0

    def __init__(self, name, score):
        # _name 表示私有变量，外部不可访问
        Student.name_id = Student.name_id + 1
        self._name = name
        self._score = score

    def print_score(self):
        Student.name_id = Student.name_id + 1
        print("name %s, score %s %d " % (self._name, self._score, Student.name_id))

    def set_score(self, score):
        self._score = score

    def get_score(self):
        return self._score


# 定义好了Student类，就可以根据Student类创建出Student的实例，创建实例是通过类名+()实现的：
bart = Student("dingbin", 100)
bart.print_score()
bart.set_score(200)
bart.print_score()
bart._score = 300
bart.print_score()


class Animal(object):
    def run(self):
        print("animal is running.......")


class Dog(Animal):
    def run(self):
        print("dog is running......")


animal = Animal()
animal.run()
dog = Dog()
dog.run()
print(isinstance(dog, Dog))
print(isinstance(animal, Dog))

# 获取对象信息

# 我们来判断对象类型，使用type()函数： type(123)==type(456)
print(type(dog))
print(type(123))
# 能用type()判断的基本类型也可以用isinstance()判断：

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print(dir(dog))
# >>> hasattr(obj, 'y') # 有属性'y'吗？
print(hasattr(dog, "name"))
print(hasattr(bart, "_name"))

# 实例属性和类属性
bart.print_score()
