def check_age(age):
    """
    :param age: 年龄
    :return: 是否成年
    """
    if age>=18:
        return "成年人"
    return None

result = check_age(18)
if not result :
    print("未成年")
else:
    print("成年")


def print1():
    print("print1")
def print2():
    print("print2")
def print3():
    print1()
    print("print3")
def print4():
    print("print4")

def  printx():
    print1()
    print2()
    print3()
printx()