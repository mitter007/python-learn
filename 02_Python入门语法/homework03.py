name="传播止咳"
set_up_year= 2006
print("我是：" +name +",我成立于：%d"%set_up_year)# TypeError: can only concatenate str (not "int") to str
# 我是：传播止咳,我成立于：2006

class_num=57
avg_salary= 16781
stock_price=13.35
message ="python,北京%s期，毕业平均薪资%s"%(class_num,avg_salary)
message1 ="python,北京%d期，毕业平均薪资%s"%(class_num,avg_salary)
message2 ="python,北京%d期，毕业平均薪资%d,今天的股价是%f"%(class_num,avg_salary,stock_price)
message3 ="python,北京%d期，毕业平均薪资%s,今天的股价是%f"%(class_num,avg_salary,stock_price)
print(message)# python,北京57期，毕业平均薪资16781
print(message1)
print(message2)
print(message3)

# s是string的占位符

# 数字精度控制

print("*********************")
num1 = 11
num2=11.345
print("%d"%num1)#
print("%d"%(num1))#
print("%1d"%num1)#
print("%4d"%num1)#
print("%4d"%num2)#
print("%4.2f"%num2)#
print("%7.2f"%num2)#
print("%2.2f"%num2)#
print("%5.2f"%num2)#
print("%4.3f"%num2)#
print("%4.0f"%num2)#
