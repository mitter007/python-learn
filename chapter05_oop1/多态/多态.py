# 应用
# 需求：
#
# ①在Dog类中封装方法game：普通狗只会简单地玩耍。
# ②定义XiaoTianQuan继承Dog，并重写game方法：哮天犬需要在天上玩耍。
# ③定义Person类，并且封装一个和狗玩的方法：在方法内部，直接让狗对象调用game方法。


class Dog():
    def  game(self):
        print("普通狗只会简单地玩耍")
class XiaoTianQuan(Dog):
    def game(self):
        print("哮天犬会玩耍")
class  Person():

    def __init__(self):
        self.Dog=None
    def  play_with_dog(self):
        self.Dog.game()
leijun =Person()
Person.Dog = leijun
xiaotianquan=XiaoTianQuan()
leijun.play_with_dog()