class Cat:
    def __init__(self,name):
        print("这是init方法")
        self.name =name
    def eat(self):
        print("%s吃饭了" % self.name)
    def speak(self):
        print("%s说话了" % self.name )
    def __del__(self):
        print("%s 拜拜" % self.name)
tom =Cat("tom")
tom2 =Cat("jerry")

tom.eat()
tom2.speak()