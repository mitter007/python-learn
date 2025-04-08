# 创建类：
class Cat:
    def eat(self):
        print("%s爱吃鱼" % self.name)  # 哪一个对象调用的方法，self就是哪一个对象的引用。

# 创建对象：
tom = Cat()
tom.name = "tom"  # 增加属性
tom.eat()

#再创建一个对象
lazy_tom = Cat()
lazy_tom.name = "懒猫"  # 增加属性
lazy_tom.eat()
