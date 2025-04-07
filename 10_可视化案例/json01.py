# 导入json模块
import json

# 准备符合格式json格式要求的python数据
data = [{"name": "老王", "age": 16}, {"name": "张三", "age": 20}]
print(data)

# 通过 json.dumps(data) 方法把python数据转化为了 json数据
data = json.dumps(data)
print(data)
# 通过 json.loads(data) 方法把json数据转化为了 python数据
data = json.loads(data)
print(data)

