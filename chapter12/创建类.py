# 创建类：
class Cat:
    def eat(self, ):
        print("小猫爱吃鱼")
    def drink(self, ):
        print("小猫爱喝水")

# 创建对象：
tom = Cat()

tom.eat()
tom.drink()
print(tom)

#再创建一个对象
lazy_tom = Cat()

lazy_tom.eat()
lazy_tom.drink()
print(lazy_tom)

kitty = lazy_tom
print(kitty)

class Cat1:
    def __init__(self):
        print("这是初始化方法")

# 使用类名创建对象，自动初始化
tom = Cat1()
