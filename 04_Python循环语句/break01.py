for i in range(1,101):
    print(f"今天是和小美在一起的第{i}天")
    print("早餐")
    print("午餐")
    if int(input("请输入0或1：")==1):
        print("今天小美心情不好，不送晚餐了")
        break
    print("晚餐")

print("表白成功了")