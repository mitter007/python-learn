import random
import uuid

# dates = ["2011-01.py-01.py", "2011-01.py-02", "2011-01.py-03", "2011-01.py-04", "2011-01.py-05", "2011-01.py-06", "2011-01.py-07", "2011-01.py-08"
#          , "2011-01.py-09", "2011-01.py-10", "2011-01.py-11", "2011-01.py-12", "2011-01.py-13", "2011-01.py-14", "2011-01.py-15", "2011-01.py-16"
#          , "2011-01.py-17", "2011-01.py-18", "2011-01.py-19", "2011-01.py-20", "2011-01.py-21", "2011-01.py-22", "2011-01.py-23", "2011-01.py-24"
#          , "2011-01.py-25", "2011-01.py-26", "2011-01.py-27", "2011-01.py-28", "2011-01.py-29", "2011-01.py-30", "2011-01.py-31"]
dates = ["2011-02-01.py", "2011-02-02", "2011-02-03", "2011-02-04", "2011-02-05", "2011-02-06", "2011-02-07", "2011-02-08"
         , "2011-02-09", "2011-02-10", "2011-02-11", "2011-02-12", "2011-02-13", "2011-02-14", "2011-02-15", "2011-02-16"
         , "2011-02-17", "2011-02-18", "2011-02-19", "2011-02-20", "2011-02-21", "2011-02-22", "2011-02-23", "2011-02-24"
         , "2011-02-25", "2011-02-26", "2011-02-27", "2011-02-28"]

provinces = ["安徽省", "河南省", "江苏省", "福建省", "广东省", "广西省", "湖北省", "湖南省", "山东省", "山西省", "河北省",
             "陕西省", "浙江省", "贵州省", "云南省", "四川省", "辽宁省", "江西省"]

f = open("C:\\Users\\caoyu\\Desktop\\2011年2月销售数据JSON.txt", "w", encoding="UTF-8")
for d in dates:
    base_num = random.randint(30, 36)
    if d == '2011-02-02' or d == '2011-02-03':
        base_num = random.randint(60, 66)
    for i in range(base_num):
        oid = str(uuid.uuid4())
        money = random.randint(100, 3000)
        province = provinces[random.randint(0, len(provinces) - 1)]
        msg = '{"date": "%s", "order_id": "%s", "money": %d, "province": "%s"}' % (d, oid, money, province)
        f.write(msg)
        f.write("\n")

f.close()

