# global money
money =5000000
global name
name =input("请输入您的姓名：")
global result
print(f"{name},您好，欢迎来到黑马银行ATM。请选择操作")

def check_money():
    return money
def get_money(count):
    global money
    money-=count
    return money
def add_money(count):
    # m=money
    global money
    money= money+count
    return money
def exit(code):
    if code ==4:
      global result
      result = 0
result =1
while result:
    print("查询余额\t【输入1】")
    print("存款\t【输入2】")
    print("取款\t【输入3】")
    print("退出\t【输入4】")
    x = int(input("请输入您的选择："))
    if x == 1:
        print(f"{name}您好，您的余额是{money}元")
    elif x == 2:
        count = int(input("请输入您的存款金额："))
        add_money(count)
        print(f"{name}您好，您的余额是{money}元")
    elif x == 3:
        count = int(input("请输入您的取款金额："))
        get_money(count)
        print(f"{name}您好，您的余额是{money}元")
    elif x == 4:
        print("退出")
        exit(4)
    else:
        print("输入数字有误")










