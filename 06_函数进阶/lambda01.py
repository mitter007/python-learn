def add(x,y=7):
    return x + y

def add2(add):
    return add(1)+1
result=add2(add)
print(result)
# 缺省参数（默认值）
def user_info(name, age, gender='男'):
    print(f"姓名是:{name}, 年龄是:{age}, 性别是:{gender}")

user_info('小天', 13)