# 导入时间模块
import time
print("开始")
# 让程序睡眠1秒(阻塞)
time.sleep(1)
print("结束")


# 导入时间模块中的sleep方法
from time import sleep
print("开始")
# 让程序睡眠1秒(阻塞)
sleep(1)
print("结束")

# 导入时间模块中的所有方法
from time import *
print("开始")
# 让程序睡眠1秒(阻塞)
# time.sleep(1) # 这种写法错误
print("结束")

# 模块别名
import time as tt
tt.sleep(2)
print('hello')
# 功能别名
from time import sleep as sl
sl(2)
print('hello')


# 注意事项：当导入多个模块的时候，且模块内有同名功能. 当调用这个同名功能的时候，调用到的是后面导入的模块的功能
from my_module2 import  test_b
from  my_module1 import test_b
print(test_b(1,2))


