# （2）私有属性和私有方法
# 在实际开发中，对象的某些属性或方法 可能只希望 在对象的内部使用，而不希望在外部被访问到
# class Women:
#     def __init__(self, name):
#         self.name = name
#         self.age = 18
#     def secret(self):
#         print("%s的年龄是%d" % (self.name, self.age))
#
# Yilia = Women("Yilia")
# Yilia.secret() # AttributeError: 'Women' object has no attribute 'age'
# print(Yilia.age)


# 在定义属性或方法时，在 属性名或者方法名前 增加 两个下划线，定义的就是私有属性或者方法。
# 例如：__age

class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        print("%s的年龄是%d" % (self.name, self.age))

Yilia = Women("Yilia")
Yilia.__secret()


#   伪私有属性和私有方法（科普）
#   python中没有真正意义上的私有。
#
#   在python开发中 不要使用 这种方式访问对象的私有属性或私有方法。以下内容仅限了解：
#   将上述报错的语句进行修改，就会发现程序可以正常执行了：
#   将print(Yilia.__age)改为print(Yilia._Women__age)
#   将Yilia.__secret()改为Yilia._Women__secret()
