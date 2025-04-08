class Houseitem:
    def __init__(self,name,area):
        self.name = name
        self.area = area
    def __str__(self):
        return '%s 占地 %s。' % (self.name, self.area)
class house:
    def __init__(self,name,square,Houseitem):
        self.name = name
        self.square =square
        self.Houseitem=[]
    # def add_houser_item(self,Houseitem):


