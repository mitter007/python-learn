"""
*args
*args 用于传递 任意数量的位置参数。它将所有传入的非关键字参数收集到一个元组中，供函数使用。

args 是一个惯例名称，你可以用其他名称代替它（例如 *params），但是约定俗成使用 args。
"""
def my_function(*args):
    for arg in args:
        print(arg)

# 在 Python 中，*args 和 **kwargs 是用于函数定义中的特殊语法，它们允许你传递可变数量的参数。
# 它们在函数定义时非常有用，尤其是在你不知道将要传递多少个参数时。


# 调用函数时传入任意数量的参数
my_function(1, 2, 3, 'hello', True)

"""
2. **kwargs
**kwargs 用于传递 任意数量的关键字参数（即以键值对形式传递的参数）。它将所有传入的关键字参数收集到一个字典中，供函数使用。

kwargs 是一个惯例名称，同样你也可以用其他名称代替（例如 **params），但是通常使用 kwargs。
"""
def my_function1(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# 调用函数时传入任意数量的关键字参数
my_function1(name="John", age=25, job="Engineer")


# 3. *args 和 **kwargs 一起使用
# 你可以在同一个函数中同时使用 *args 和 **kwargs，但是它们的顺序需要遵循 *args 放在前，**kwargs 放在后。这样，函数可以同时接收位置参数和关键字参数。


def my_function2(arg1, *args, kwarg1=None, **kwargs):
    print(arg1)
    print(args)
    print(kwarg1)
    print(kwargs)

# 调用函数时传递位置参数和关键字参数
my_function2(1, 2, 3, 4, kwarg1='hello', name='John', age=25)
