# ①在Dog类中封装方法game：普通狗只会简单地玩耍。
# ②定义XiaoTianQuan继承Dog，并重写game方法：哮天犬需要在天上玩耍。
# ③定义Person类，并且封装一个和狗玩的方法：在方法内部，直接让狗对象调用game方法。

class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s在蹦蹦跳跳地玩耍" % self.name)


class XiaoTianQuan(Dog):
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s在天上玩耍" % self.name)


class Person(object):
    def __init__(self, name):
        self.name = name

    def play_with_dog(self, dog):
        dog.game()
        print("%s和%s在玩耍" % (self.name, dog.name))

# 创建一个狗对象
laipi = XiaoTianQuan("赖皮")
xiaohui = Dog("小灰")

# 创建一个人对象
Yilia = Person("Yilia")

# 让人和狗玩耍
Yilia.play_with_dog(laipi)
Yilia.play_with_dog(xiaohui)


# 赖皮在天上玩耍
# Yilia和赖皮在玩耍
# 小灰在蹦蹦跳跳地玩耍
# Yilia和小灰在玩耍