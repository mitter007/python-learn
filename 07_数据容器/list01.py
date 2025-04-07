name1 = '王力宏'
name2='周杰轮'
name3='林俊杰'
name4='张学友'
name5='刘德华'
name_list1=['n1','n2','n3','n4','n5']
print(name_list1) # ['n1', 'n2', 'n3', 'n4', 'n5']
type=type(name_list1)
print(type) #<class 'list'>

name_list2=[name1,name2,name3]
name_list3=[name4,name5]
name_lists=[name_list1,name_list2,name_list3]
print(name_lists)

x=name_list1[0]
y=name_list1[-1]
print(x)
print(y)
print(name_lists[1])

# 嵌套list元素的取出
print(name_lists[0][0])
print(name_lists[0][0]) # IndexError: list index out of range 角标越界

name_list5=[]
print(name_list5)

print("***************************")
name_list5.append("1")
name_list5.append('2')
name_list5.append(3)
name_list5.index(3)
print(name_list5.index(3))
print(name_list5.index('1'))
# print(name_list5.index('3')) # ValueError: '3' is not in list
print(name_list5)
print("***********************************")
my_list=[1,2,3,4,5,6,7,8]
my_list.insert(0,'itheima')
my_list.append('sgg')


# 追加元素 并添加到list的尾部
my_list.extend(['9','10','11','12','13','14',''])

# 删除元素

del my_list[0]
del my_list[0]
my_list.pop(0)
# my_list.pop()
# 删除某元素在列表中的第一个匹配项
my_list.remove('sgg')
my_list.remove('')
# 清空列表内容
# my_list.clear()

# 统计某元素在列表内的数量
my_list.count(1)
print(my_list.index(3))

my_list.insert(0,3)
print(my_list.count(3))
print(my_list)

len(my_list)
print(len(my_list)) # 13
