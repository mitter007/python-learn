# Python 支持多重继承（一个子类可以同时继承多个父类），这是 Python 与 Java 在继承机制上的重要区别之一。不过，多重继承虽然强大，但也容易导致代码复杂性增加，因此需要谨慎使用。

class Parent1:
    def method1(self):
        print("Parent1 的 method1")
    def methodq(self):
        print("Parent1 的 method2")

class Parent2:
    def method2(self):
        print("Parent2 的 method2")
    def methodq(self):
        print("Parent2 的 method2")
# Child 同时继承 Parent1 和 Parent2
class Child(Parent1, Parent2):
    def child_method(self):
        print("Child 自己的方法")

# 使用
obj = Child()
obj.method1()  # 继承自 Parent1
obj.method2()  # 继承自 Parent2
obj.child_method()
obj.methodq() # Parent2 的 method2