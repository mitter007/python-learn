age = int(input("请输入您的年龄:"))
year= int(input("入职年限:"))
level = int(input("等级:"))


if age >= 18:
    print("成年人符合，继续判断")
    if age < 30:
        print("年龄达标继续判断")
        if year > 2:
            print("小于30岁的成年人且入职超过2年，满足条件，可以领取")
        elif level > 3:
            print("级别大于3的成年人可直接领取礼物")
        else:
            print("Sorry，年龄符合，但入职时间不足")
    else:
        print("您的年龄过大或级别小于等于3，不可领取")
else:
    print("Sorry，未成年不可领取礼物")