print("欢迎来到黑马动物园")

# vip_level=int(input("请输入你的vip级别：(1~5)"))
if  int(input("请输入您的身高(cm):"))>120:
    print("您的身高大于120cm，需要付费")
    print("不过您的vip等级大于3可以免费游玩")
    if int(input("请输入你的vip级别：(1~5)"))>3:
        print("您可以免费游玩")
        print("祝您游玩愉快")
    else :
        print("您需要付费")
else :
    print("您的身高小于120cm，可以免费游玩")
    print("祝您游玩愉快")
