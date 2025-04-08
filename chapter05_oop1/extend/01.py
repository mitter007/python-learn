# extends


# 继承可以实现代码的重用，相同的代码不需要重复地编写。
# 子类 拥有 父类 的所有 方法 和 属性。

# 单继承
#
# 一个子类只有一个父类

# 多继承
#
# 一个子类可以有多个父类


# class 类名(父类名):
#     pass
class Animal:
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")
    def run(self):
        print("跑")
    def sleep(self):
        print("睡")

class Dog(Animal):
    def bark(self):
        print("汪汪汪")

#创建一个对象——狗对象
laipi = Dog()
laipi.eat()
laipi.drink()
laipi.run()
laipi.sleep()
laipi.bark()


class Dog1(Animal):
   def eat(self):
       print("dog eat")
dog1 =Dog1()

dog1.eat()  # dog eat