my_list = ['黑马程序员', '传智播客', '黑马程序员', '传智播客', 'itheima', 'itcast', 'itheima', 'itcast', 'best']
set1=set()  # set1={} 这样定义不行
for i in my_list:
    print(i)

for i in my_list:
   set1.add(i)
print(set1)
# print(set1.remove('x'))
set1.remove("x")
print(set1)