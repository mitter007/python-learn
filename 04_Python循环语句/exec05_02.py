name ="itheima is a brand of itcast"
i=0
for x in name:
    if x=='a':
        i+=1
print(f"总工有{i}个a")

# range 第一种
for x in range(5):
    print(x)
print("***********************")
#  range 第二种
for x in range(5,7):
    print(x)
print("***********************")
for x in range(5,20,3):
    print(x)
print("***********************")
for x in range(5,20,4):
    print(x)