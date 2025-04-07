"""
演示函数作为参数传递
"""

# 定义一个函数，接收另一个函数作为传入参数
def test_func(yy):
    result = yy(1, 2)  # 确定compute是函数
    print(f"compute参数的类型是:{type(compute)}")
    print(f"计算结果：{result}")

# 定义一个函数，准备作为参数传入另一个函数
def compute(x, y):
    return x + y
# 调用，并传入函数
test_func(compute)


print("******************************")
# 不定长 - 位置不定长, *号
# 不定长定义的形式参数会作为元组存在，接收不定长数量的参数传入
def user_info(*args):
    print(f"args参数的类型是：{type(args)}，内容是:{args}")

user_info(1, 2, 3, '小明', '男孩')

# 不定长 - 关键字不定长, **号
def user_info(**kwargs):
    print(f"args参数的类型是：{type(kwargs)}，内容是:{kwargs}")
user_info(name='小王', age=11, gender='男孩')
