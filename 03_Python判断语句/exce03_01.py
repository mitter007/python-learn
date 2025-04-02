high=int(input("欢迎来到黑马动物园。\n"
                 "请输入您的身高(cm):"))
vip_level=int(input("请输入你的vip级别：(1~5)"))
if  high<=120:
    print("您的身高未超过120cm，可以免费游玩")
elif vip_level>=3:
    print("您的vip级别大于3，可以免费游玩")
elif 1==1:
    print("您可以继续游玩")
else :
    print("您的身高超过120cm，游玩需要购票10元。")

print("祝您游玩愉快")