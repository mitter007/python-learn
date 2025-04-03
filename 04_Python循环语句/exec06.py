num =100
i = 0

print("************************")
for x in range(1,num):
    if x%2==0:
      i+=1
print(f"总共有{i}个偶数")
print(x)

"""
# 定义一个数字变量num，内容随意
num = 20  # 这里我设置为20，你可以改成任意数字

# 初始化偶数计数器
even_count = 0

# 使用range()获取从1到num的序列，并用for循环遍历
for number in range(1, num + 1):
    # 判断是否为偶数
    if number % 2 == 0:
        even_count += 1  # 如果是偶数，计数器加1

# 打印结果
print(f"在1到{num}之间，共有{even_count}个偶数")
"""