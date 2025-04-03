def add(x,y):
    retult =x+y
    return retult
result= add(3,4)
print(result)


def fun():
    print("xx")
x=fun()
y=type(x)
print(x)
print(y)# <class 'NoneType'>

def check_age(age):
    if age>=18:
        return "成年人"
    return None

result = check_age(5)
if not result :
    print("未成年")