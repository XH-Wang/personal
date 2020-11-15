# coding:utf-8
import os
import filecmp

# 输入路径
path   = input("Please Enter Path:") 
suffix = input("Please Enter suddix:")

if suffix[0] != ".":
    suffix = "." + suffix

# 遍历所有文件，获取指定后缀的文件列表
file_ls = []

for root, dirs, files in os.walk(path):
    # 遍历文件
    for f in files:
        cur_path = os.path.join(root, f)

        if os.path.splitext(cur_path)[1].lower() == suffix.lower():
            file_ls.append(cur_path)
            print("Find file: " + cur_path)
            continue

option = input("\nDelete all files?[Y/N]") 

# 若选择删除则删掉重复文件列表中的所有文件
if option == "Y":
    for f in file_ls:
        os.remove(f)
        print("delete file:" + f)
else:
    print("All file keep.")

input("\ncompleted.")