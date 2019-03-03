import os
#1.获取用户文件夹输入
file_name = input("请输入您要重命名的文件夹：")


#2.获取所有文件名
file_names = os.listdir(file_name)

#第一种方法
os.chdir(file_name) #跳进当前目录才能重命名

#3.修改文件名



for name in file_names:
    #print(name)

    num = len("[东哥出品]-")#有缺陷 当删完了会删除别的信息
    #print(num)#for test
    new_name = name[num:]
    os.rename(name,new_name)
