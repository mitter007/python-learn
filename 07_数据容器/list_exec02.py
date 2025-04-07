my_list = [1, 2, 3, 4, 5,6,7,8,9,10]
new_list1 = []
new_list = []
i = 0
while i < len(my_list):
    if my_list[i] % 2 == 0:
        new_list.append(my_list[i])
    i+=1
print(new_list)

print("****************************")

# for 循环 j是my_list中的元素
for j in my_list:
    if j % 2 == 0:
        new_list1.append(j)
print(new_list1)