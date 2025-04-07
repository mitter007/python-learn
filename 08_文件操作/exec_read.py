f = open(r'bill.txt', 'r', encoding="UTF-8")
f.readline()

for line in open('bill.txt', 'r', encoding="UTF-8"):

    x=line.strip().split(',')
    print(x)
    print(x.count('测试'))
    if x.count('测试')!=0:
        print(x)
        f = open(r'bill-apk.txt', 'w', encoding="UTF-8")
        f.write(line)
        f.close()
