class Cat:
    def __init__(self):
        print("这是初始化方法")
        self.name = "tom"
    def eat(self):
        print("%s爱吃鱼" % self.name)

# 使用类名创建对象
tom = Cat()
tom.eat()
print(tom.name)
