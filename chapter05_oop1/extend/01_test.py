class Animal:
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")
    def run(self):
        print("跑")
    def sleep(self):
        print("睡")

class Cat(Animal):
    def bark(self):
        print("喵喵喵")
class Dog(Animal):
    def bark(self):
        print("汪汪汪")
# class XiaoTianQuan(Dog):
#     def fly(self):
#         print("I can fly")
#
#     #     父类方法的重写
#     def bark(self):
#         print("叫的跟神一样")
#         #2、使用super()调用原本在父类中封装的方法
#         super().bark()
#
#         #3、其他子类的代码
#         print("!#$^$%^%^*")

class XiaoTianQuan(Dog):
    def bark(self):
        XiaoTianQuan.bark(self)


#创建一个对象——狗对象
laipi = XiaoTianQuan()
laipi.eat()
laipi.drink()
laipi.run()
laipi.sleep()

print("*"*50)
laipi.bark()
laipi.fly()
