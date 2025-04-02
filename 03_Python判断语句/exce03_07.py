import random
#deepseek的回答
# 生成随机数字
num = random.randint(1, 10)

# 第一次猜测
guess = int(input("第1次猜测，请输入1-10的数字："))
if guess == num:
    print("恭喜你，猜对了！")
else:
    if guess > num:
        print("猜大了")
    else:
        print("猜小了")

    # 第二次猜测
    guess = int(input("第2次猜测，请输入1-10的数字："))
    if guess == num:
        print("恭喜你，猜对了！")
    else:
        if guess > num:
            print("猜大了")
        else:
            print("猜小了")

        # 第三次猜测
        guess = int(input("第3次猜测，请输入1-10的数字："))
        if guess == num:
            print("恭喜你，猜对了！")
        else:
            print(f"很遗憾，游戏结束。正确答案是：{num}")