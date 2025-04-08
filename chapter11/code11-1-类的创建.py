class Player(object): # object 基类
    pass

tom = Player()  # 类的实例化（创建对象）
print(type(tom))
# isinstance() 是 Python 中一个非常实用的内置函数，用来判断一个对象是不是某种类型或某些类型之一。
# 基本语法
# isinstance(object, classinfo)
print(isinstance(tom,object))
print(isinstance(tom,Player))