f = open(r'D:\02_code\pythonCode\python-learn\data\word.txt', 'r', encoding="UTF-8")
x = f.read()
# x=f.readlines()
print(x)
print(type(x))

print(x.count("itheima")) #6
f.close()

from pathlib import Path

file_path = Path("D:/02_code/pythonCode/python-learn/data/word.txt")
with file_path.open("r", encoding="UTF-8") as f:
    content = f.read()

print(content)