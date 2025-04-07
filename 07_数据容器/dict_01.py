# dict02={'x':1,'t':2}
# print(dict02)
# y=dict02.keys()
# print(y) # dict_keys(['x', 't'])
#
# dict03={'key03':dict02}
# key03=dict03.keys()
# print(key03)
dict01={'部门':'科技部','工资':3000,'级别':1}
dict02={'部门':'市场部','工资':5000,'级别':2}
dict03={'部门':'市场部','工资':7000,'级别':3}
dict04={'部门':'科技部','工资':4000,'级别':1}
dict05={'部门':'市场部','工资':6000,'级别':2}

print(dict01.keys())
print(dict02.keys())
print(dict03.keys())
print(dict04.keys())
print(dict05.keys())


dict06={
    '王力宏':dict01,
    '周杰伦':dict02,
    '林俊杰':dict03,
    '张学友':dict04,
    '刘德华':dict05
}

print(dict06)
print(dict06.keys())

dict01={
    '王力宏':{'部门':'科技部','工资':3000,'级别':1},
    '周杰伦':{'部门':'市场部','工资':5000,'级别':2},
    '林俊杰':{'部门':'市场部','工资':7000,'级别':3},
    '张学友':{'部门':'科技部','工资':4000,'级别':1},
    '刘德华':{'部门':'市场部','工资':6000,'级别':2}
}
# print(dict01)
# keys=dict01.keys
# print(keys)
for key in (dict06.keys()):
    print(dict06[key])
    print(dict06[key]['工资'])
    if dict06[key]['级别']==1:
        dict06[key]['级别']=2
        x=dict06[key]['工资']
        dict06[key]['工资']=x+1000
    # print(dict01.get(key))
 # if  dict06[key]['级别'] == 1:
 #     dict06[key]['级别'] =2
 #     dict06[key]['工资'] =dict06["key"]['工资'] +1000

print('*******************')
print(f"dict06:{dict06}")



