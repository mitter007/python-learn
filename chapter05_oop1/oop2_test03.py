class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s]占地%.2f" % (self.name, self.area)

class House:
    def __init__(self, Type, square):
        self.Type = Type
        self.square = square
        self.left_square = square
        self.HouseItem = []

    def __str__(self):
        return ("户型：【%s】\n总面积：【%d】 m²\n剩余面积：【%.02f】 m²\n家具名称列表%s"
                % (self.Type, self.square, self.left_square, self.HouseItem))
        """
    python能够自动地将一对括号内部的代码连接在一起
        """

    def add_furniture(self, item):
        print("要添加%s m²" % item)
        if item.area <= self.left_square:
            self.HouseItem.append(item.name)
            self.left_square -= item.area
        else:
            print("sorry, %s的面积超过了剩余面积，摆不下" % item.name)
            return


# 创建家具
bed = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("桌子", 1.5)
print(bed)
print(chest)
print(table)

# 创建房子对象
my_home = House("两室一厅", 60)
# my_home = House("两室一厅")
# 添加家具
my_home.add_furniture(bed)
print(my_home.left_square)
my_home.add_furniture(chest)
print(my_home.left_square)
my_home.add_furniture(table)
print(my_home.left_square)
print(my_home)
