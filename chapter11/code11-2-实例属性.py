class Player(object):
    def __init__(self,name,age,city):  # 初始化函数（构造函数）
        self.name = name
        self.age = age
        self.city = city

mia = Player('mia',24,'上海')
mia.city = '杭州'
tom = Player('tom',34,'重庆')
tom.height = 180
tom.age = 32
print(tom.__dict__) # 获取实例（对象）的所有属性

print('* '*50)

# 武器： 名字 攻击值 等级
class weapon(object):
    def __init__(self,name,damage,level):
        self.name = name
        self.damage = damage
        self.level = level

gun = weapon('magic',1000,3)
print(gun.__dict__)

print('* '*50)

class Gun(object):
    def __init__(self,name,count,bullet):
        self.name = name
        self.count = count
        self.bullet = bullet
gun1=Gun('枪',200,12)

gun.model=3
print(gun.__dict__)  # {'name': 'magic', 'damage': 1000, 'level': 3, 'model': 3}