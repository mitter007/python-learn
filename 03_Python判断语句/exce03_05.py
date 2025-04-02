age = int(input("请输入您的年龄:"))
year= int(input("入职年限:"))
level = int(input("等级:"))

# vip_level=int(input("请输入你的vip级别：(1~5)"))
if age>=18:
    if age <30:
        if year>2:
            print("恭喜你，获奖了")
        elif level>3:
            print("恭喜你，获奖了")
        else:
            print("没获奖")
    else:
        print("没获奖")
else:
    print("没获奖")