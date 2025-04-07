age_list=[21,25,21,23,22,20]
age_list.append(31)
age_list.extend([29,33,30])
# age_list.index(0)
# print(age_list[0])
# print(age_list[-1])
# print(age_list.index(31)) #6
# print(age_list)


# list的遍历
i = 0
while i<len(age_list):
    print(age_list[i])
    i +=1

print("**********************")
for x in age_list:
    print(x)