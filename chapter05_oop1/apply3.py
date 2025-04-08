# 一个对象的属性，可以是另一个类创建的对象
# None关键字表示 什么都没有，表示一个 空对象，没有方法和属性，是一个特殊的常量。可以将None赋值给任何一个变量。

# 题目：
# 士兵许三多有一把AK47，士兵可以 开火。
# 枪能够发射子弹，枪装填子弹——增加子弹数量

class Gun:
    def __init__(self,name,bullets):
        self.name = name
        self.bullets=bullets
        self.left_bullets=bullets
    def shoot(self):
        if self.bullets<=0:
            print("请装填子弹")
        self.bullets -=1
    def fill_bullet(self,count):
        self.bullets +=count


class Soldier:
    def __init__(self,name):
        self.name = name
        # self.Gun.bullets=60  # AttributeError: 'Soldier' object has no attribute 'Gun'

# 一个对象的属性，可以是另一个类创建的对象
# None关键字表示 什么都没有，表示一个 空对象，没有方法和属性，是一个特殊的常量。可以将None赋值给任何一个变量。
        self.Gun =None
soldier=Soldier('Bob')

AK47=Gun('ak-47',60)
soldier.Gun=AK47
AK47.shoot()
AK47.shoot()
AK47.fill_bullet(9)
print(soldier.Gun.bullets)

