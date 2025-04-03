import random
num = random.randint(1, 100)
i=1
x=int(input("请输入数字："))
while x!=num:
    if x>num:
        print("大了")
    else:
        print("小了")
    print("猜错啦，请继续输入：")
    x = int(input())
    i=i+1
if x==num:
    print("恭喜你猜对啦,您猜了%d次"%i)

