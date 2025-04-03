num =100
"""
def test1():
    print(num)

def test3(x):
    num=400+x
    print(num)
def test2():
    num =200
    print(num)
# 如何将函数内定义的变量声明为全局变量

test3(3)
test2()  #200
print(num) #100
"""

money =5000000
name =input("请输入您的姓名：")
print(f"{name},您好，欢迎来到黑马银行ATM。请选择操作")

def get_money(count):
    money=money+200
    return money

def check_money():
    return money
def add_money(count):
    # m=money
    global money
    money= money+count
    return money
