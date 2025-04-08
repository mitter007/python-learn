class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return "我的名字叫%s，体重是%.2f公斤" % (self.name, self.weight)

    def run(self):
        print("%s的体重是%.2f" % (self.name, self.weight))
        self.weight -= 0.5

    def eat(self):
        print("%s的体重是%.2f" % (self.name, self.weight))
        self.weight -= 1


Yilia = Person("Yilia", 47.0)
Yilia.run()
Yilia.eat()
print(Yilia)

dudu = Person("dudu", 85.0)
dudu.run()
dudu.eat()
print(dudu)