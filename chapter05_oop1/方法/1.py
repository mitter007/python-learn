class Tool(object):

    # 定义类属性
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1  # 通过`类名.count`调用类属性，让类属性+1


# 创建对象
futou = Tool("斧头")
liandao = Tool("镰刀")
chutou = Tool("锄头")

#输出工具总数
print(Tool.count)
