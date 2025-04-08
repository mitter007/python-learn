class Cat:
    def __init__(self):
        print("这是初始化方法")
        self.name = "tom"
        self.hobbit=1
    def eat(self):
        print("%s爱吃鱼" % self.name)

    def sleep(self):
        print("%s爱睡觉" % self.name)

# 使用类名创建对象
tom = Cat()
tom.eat()

tom2=Cat()
tom2.eat()
tom2.sleep()
tom3=tom2
print(tom2)  # <__main__.Cat object at 0x0000019B10BD1810>
print(tom3)  # <__main__.Cat object at 0x0000019B10BD1810>
print(tom3.hobbit) # 1

