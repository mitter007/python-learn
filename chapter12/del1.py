class Cat:
    def __init__(self, new_name):
        print("这是初始化方法")
        self.name = new_name

    def eat(self):
        print("%s爱吃鱼" % self.name)

    def __del__(self):
        print("%s 拜拜" % self.name)

#  这是个很好的问题！Python 中像 __str__ 这种带有前后双下划线的方法，
    #  被称为 “魔术方法”（magic methods）或 “特殊方法”（special methods）。它们是
 #   Python 内部用来实现某些功能的特殊钩子方法，通常不会在用户代码中直接调用，而是通过特定的操作间接触发。
    def __str__(self):
       return "我是小猫【%s】" % self.name

# 使用类名创建对象
tom = Cat("Tom")
tom.eat()
# del tom

print(tom) # 我是小猫【Tom】
print("*" * 50)


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person named {self.name}"

p = Person("Alice")
print(p)  # 自动调用 p.__str__()，输出：Person named Alice

