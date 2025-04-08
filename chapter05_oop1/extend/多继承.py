# 多继承
# 子类可以有多个父类，并且具有 所有父类 的 属性和方法
# 如：孩子会继承自己父亲和母亲的特性
"""

（2）多继承的使用注意事项
如果不同的父类中存在同名的方法，子类对象在调用方法时，会调用哪一个父类？

python中的MRO——方法搜索顺序
python中针对 类 提供了一个 内置属性__mro__，可以查看 方法 搜索顺序。MRO（method resolution order），主要用于 在多继承时判断方法、属性 调用路径。
例如：
print(c.__mro__)
输出结果：
(<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)按照__mro__输出顺序从左向右依次查找。如果找到将不再继续搜索，如果找到最后一个类，还没有找到方法，程序报错。

开发时应该尽量避免这种容易产生混淆的情况。如果父类之间存在同名的属性或者方法，应该尽量避免使用多继承。

应用：
————————————————

版权声明：本文为博主原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接和本声明。

原文链接：https://blog.csdn.net/qq_44250700/article/details/120133887
"""

class A:
    def test(self):
        print("a-test")
    def demo(self):
        print("a-demo")

class B:
    def test(self):
        print("b-test")
    def demo(self):
        print("b-demo")


class C(A, B):
    pass

# 创建子类对象
c = C()
c.test()
c.demo()

print(C.__mro__)
