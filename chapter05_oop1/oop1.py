class Cat:
    def __init__(self):
        print("这是初始化方法")

# 使用类名创建对象，自动初始化
tom = Cat()

print("*" * 50)
"""
一个对象从调用类名()创建，生命周期开始
一个对象的__del__方法一旦被调用，生命周期结束
在对象的生命周期内，可以访问对象属性，或者让对象调用方法
"""


class Cat1:
    def __init__(self, new_name):
        print("这是初始化方法")
        self.name = new_name

    def eat(self):
        print("%s爱吃鱼" % self.name)

    def __del__(self):
        print("%s 拜拜1" % self.name)

# 使用类名创建对象
tom = Cat1("Tom")
tom.eat()

print("*" * 50)



class Cat2:
    def __init__(self, new_name):
        print("这是初始化方法")
        self.name = new_name

    def eat(self):
        print("%s爱吃鱼" % self.name)

    def __del__(self):
        print("%s 拜拜2" % self.name)

    def __str__(self):
        return "我是小猫【%s】" % self.name

# 使用类名创建对象
tom = Cat2("Tom")
print(tom)
