def print_file_info(file_name):
    try:
        print("xxx")
        f = open(""+file_name+"", 'r', encoding="UTF-8")
        x= f.readlines()
        print(x)
    except (FileNotFoundError) as e:
        print(e)
        print("文件找不到")
    finally:
        f.close()
def append_to_file(file_name, data):
    try:
        f = open(r""+file_name+"", 'a', encoding="UTF-8")
        x= f.write(data)
        print(x)
    except (FileNotFoundError) as e:
        print(e)
        print("文件找不到")
    finally:
        f.close()

def main():
    print("*********")
    print_file_info("write.txt")
    append_to_file("write.txt","qqqqqqqqqqqqqqqqqqqqqqqqq")
    print_file_info("write.txt")
main()