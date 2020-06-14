# coding:utf-8
import os
import filecmp

# 输入路径
path = input("Please Enter Path:") 

# 遍历所有文件，获取有用文件列表及重复文件列表
file_ls_keep = []
file_ls_rept = []

for root, dirs, files in os.walk(path):
    # 遍历文件
    for f in files:
        cur_path = os.path.join(root, f)

        if len(file_ls_keep) == 0:
            file_ls_keep.append(cur_path)
            print("Keep file: " + cur_path)
            continue

        for file_keep in file_ls_keep:
            if filecmp.cmp(file_keep, cur_path):
               file_ls_rept.append(cur_path) 
               break

            if file_keep == file_ls_keep[-1]:
                file_ls_keep.append(cur_path)
                print("Keep file: " + cur_path)
                break

# 输出重复文件列表，确认是否删除
print("\nrepeated_list")
for f in file_ls_rept:
    print(f)

option = input("\nDelete all repeated files?[Y/N]") 

# 若选择删除则删掉重复文件列表中的所有文件
if option == "Y":
    for f in file_ls_rept:
        os.remove(f)
        print("Repeated file:\"" + f + "\" deleted")
else:
    print("All file keep.")

input("\ncompleted.")