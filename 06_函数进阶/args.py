# 不定长 - 位置不定长, *号
# 不定长定义的形式参数会作为元组存在，接收不定长数量的参数传入
def user_info(*args):
    print(f"args参数的类型是：{type(args)}，内容是:{args}")

user_info(1, 2, 3, '小明', '男孩')

# 不定长 - 关键字不定长, **号
def user_info(**kwargs):
    print(f"args参数的类型是：{type(kwargs)}，内容是:{kwargs}")
user_info(name='小王', age=11, gender='男孩')

def user_info1(*args):
    print(args)
user_info1(12,14)
user_info1(12,'jerry')

def user_info2(**kwargs):
    print(type(kwargs)) # <class 'dict'>
    x= kwargs.get("age")
    print(x)
    print(kwargs)
user_info2(name='tom',age=19,id=110) # {'name': 'tom', 'age': 19, 'id': 110}