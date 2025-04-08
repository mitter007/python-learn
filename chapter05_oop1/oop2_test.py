class Person:
    def __init__(self,name,high):
        print("进入init方法")
        self.name = name
        self.high = high
    def __str__(self):
        print(f"我的名字是%s，体重是%.2f"%(self.name,self.high))
    def eat(self):
        print(f"{self.name}吃东西啦")
    def speak(self):
        print(f"{self.name} 说话啦")
    def __del__(self):
        print("再见啦")
jet=Person("jet",1.72)
jet.eat()
jet.speak()
leijun=Person("leijun",1.84)
leijun.eat()
leijun.speak()