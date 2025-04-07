t1=('周杰轮', 11, ['football', 'music'])
t1.index(11)
print(t1.index(11))

print(t1[0])
t1[2].pop(0)
# 删除football爱好

# 增加爱好
# t1[2].append("coding")
t1[2].insert(0,'coding')
print(t1)
