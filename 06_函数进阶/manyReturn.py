def returns():
    return 1
    return 2
x=returns()
print(x) # 1

# 函数的多种传参方式

def user_info(name,age,gender):
    print(f"名字是：{name}，年龄是{age}岁，性别：{gender}")
user_info("焦文涛","27","男")  # 名字是：焦文涛，年龄是27岁，性别：男
user_info("焦文涛",27,"男")  # 名字是：焦文涛，年龄是27岁，性别：男

def user_info1(name,age,gender="男"):
    print(f"名字是：{name}，年龄是{age}岁，性别：{gender}")
user_info("焦文涛",29,"男")

user_info("焦文涛",gender="男",age=29)
user_info(gender="男",age=29,name="焦文涛")
print("******************************")

# 缺省参数：缺省参数也叫默认参数，用于定义函数，为参数提供默认值，调用函数时可不传该默认参数的值（注意：所有位置参数必须出现在默认参数前，包括函数定义和调用）.
def user_info1(name,age,gender='男'):
    print(f"名字是：{name}，年龄是{age}岁，性别：{gender}")
user_info('焦文涛',29)

def get_values():
    return 1,2
x,y=get_values()
print(f"{x}+{y}") # 1+2
x=get_values()
print(x)
# x=get_values().
print(x)