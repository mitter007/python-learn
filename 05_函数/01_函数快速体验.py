"""
演示：快速体验函数的开发及应用
"""
# 需求，统计字符串的长度，不使用内置函数len()

# print("欢迎来到黑马程序员！请出示您的健康码以及72小时核酸证明，并配合测量体温！")
# print("体温测量中，您的体温是：37.3度，体温正常请进！")


str ="欢迎来到黑马程序员！请出示您的健康码以及72小时核酸证明，并配合测量体温！"
i=0
for s in  str:
    i+=1
print(i)

def welcome():
    print("欢迎来到黑马程序员！请出示您的健康码以及72小时核酸证明，并配合测量体温！")
    print("体温测量中，您的体温是：37.3度，体温正常请进！")
    return 1
x = welcome()
print(x)


def add(x,y):
    retult =x+y
    print(f"{x}+{y}={x+y}")

add(1,2)

def check(x):
    print(f"欢迎来到黑马程序员！请出示您的健康码以及72小时核酸证明，并配合测量体温！体温测量中，您的体温是：{x}度，体温正常请进！")

check(37.4)