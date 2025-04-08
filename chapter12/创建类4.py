class Cat:
    def __init__(self, new_name):
        self.name = new_name
        print("这是初始化方法")
    def eat(self):
        print("%s爱吃鱼" % self.name)

# 使用类名创建对象
tom = Cat("Tom")
tom.eat()

lazy_cat = Cat("kitty")
lazy_cat.eat()