def fun1():
    print('fun1 start')
    x= 1/0
    print('fun1 end')

def fun2():
    print('fun2 start')
    fun1()
    print('fun2 end')

def main():
    fun2()
try:
    main()
except(ZeroDivisionError) as e:
    print(e)
else:
    print("没有出现异常")
finally:
    print("无论如何都要执行")