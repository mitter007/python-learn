num=77
x=int(input("请输入数字:"))
if  x>num:
    print("大了")
elif x<num:
    print("小了")
elif x==num:
    print("恭喜你猜对啦")
# else: #如果都不
print("Sorry,全部猜错了，我想的是：%d"%num)