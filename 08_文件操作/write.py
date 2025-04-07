f = open(r'write.txt', 'w', encoding="UTF-8")
f.write("nihao")
f.write('ssssss')

# 3. 内容刷新
f.flush()
f.close()
