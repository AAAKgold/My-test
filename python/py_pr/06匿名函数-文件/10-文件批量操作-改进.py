import os
#1.获取用户文件夹输入
fold_name = input("请输入您要重命名的文件夹：")
funFlag = int(input("请输入您的需求（1 表示添加标志，2表示删除标志）:")) #1表示添加标志 2表示删除标志
string_name = input("请输入您要添加或删除的字符：")

#2.获取所有文件名
file_names = os.listdir(fold_name)

#跳进文件夹执行
os.chdir(fold_name)

#遍历输出所有文件名字
for name in file_names:
    #print(name)#for test
    if funFlag == 1:
        newName = string_name + name
    elif funFlag == 2:
        num = len(string_name)
        newName = name[num:]
    #print(newName)#for test
    os.rename(name,newName)


