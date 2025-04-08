class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count  # 装填子弹数量

    def shoot(self):
        print("%s共有【%s】发子弹" % (self.model, self.bullet_count))

        if self.bullet_count <= 0:
            print("没子弹了，请装入子弹")
            return

        self.bullet_count -= 1  # 发射子弹
        print(("战斗开始！突突突...\n经过一番激烈的战斗，【%s】还剩【%d】发子弹"
               % (self.model, self.bullet_count)))


class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        # 1、是否有枪
        if self.gun is None:
            print("%s还没有枪" % self.name)
            return

        # 2、高喊口号
        print("冲啊...%s!" % self.name)

        # 3、让枪装填子弹
        self.gun.add_bullet(10)
        # 4、让枪发射子弹
        self.gun.shoot()


# 创建枪对象
AK47 = Gun("AK47")
AK47.add_bullet(5)
AK47.shoot()

# 创建士兵对象
xusanduo = Soldier("许三多")
"""
通过把AK47这把枪给许三多，建立起Gun和Soldier的联系。
"""
# xusanduo.gun = AK47
xusanduo.fire()
print(xusanduo.gun)
