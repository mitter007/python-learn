import random
#deepseek的回答
# 发工资的问题
# 生成随机数字
num = random.randint(1, 10)
count = 10000
for i in range(1,21):
    num = random.randint(1, 10)
    if num < 5:
        print(f"{i}号员工不发工资,绩效为{num}")
        continue
    print(f"{i}号员工领到工资了，绩效为{num}")
    count-=1000
    if count<=0:
        break
print("工资发完了")