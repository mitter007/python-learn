class MyClass:
    def instance_method(self, param):
        # 通过 self 访问实例属性
        print(f"Instance method called with param: {param}")
obj = MyClass()        # 创建类的实例
obj.instance_method(10)


# 类方法 (Class Method)
# 调用实例方法
class MyClass1:
    class_variable = 0


# self 代表实例  cls代表类
    @classmethod
    def class_method(cls, param):
        cls.class_variable+=1
        # 通过 cls 访问类属性
        print(f"Class method called with param: {param}, class_variable: {cls.class_variable}")
MyClass1.class_method(20)    # 可以通过类名调用类方法
obj = MyClass1()
obj.class_method(30)       # 也可以通过实例调用类方法

print('*'*80)

# 静态方法 (Static Method)
# 虽然你没有提到静态方法，但它也是 Python 中常见的一种方法类型。静态方法不依赖于类或实例，
# 通常用于与类相关的辅助功能。它没有 self 或 cls 参数，因此无法访问类或实例的任何属性。

class MyClass2:
    class_variable = 0
    @staticmethod
    def static_method(param):
        # cls.class_variable+=1
        print(f"Static method called with param: {param}")
MyClass2.static_method(40)  # 通过类调用静态方法
obj = MyClass2()
obj.static_method(50)     # 也可以通过实例调用静态方法


"""
关键点：
无 self 和 cls 参数：静态方法既不能访问实例属性，也不能访问类属性。

与类实例无关：静态方法通常用于那些与类或实例没有直接关系的功能。

总结：
实例方法：以 self 作为第一个参数，与类的实例绑定。通过实例调用，访问实例属性。

类方法：以 cls 作为第一个参数，与类本身绑定。通过类名或实例调用，访问类属性。

静态方法：不依赖于实例或类，通常用于类的辅助功能。

通过理解这三种方法的区别，你可以根据实际需要选择使用哪种方法。
"""
