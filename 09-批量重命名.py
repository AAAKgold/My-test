import os

#1.获取一个要重命名的文件夹的名字
folder_name = input("请输入要重命名的文件夹：")

#2.获取那个文件夹中的所有文件名
file_names = os.listdir(folder_name)

#第一种
os.chdir(folder_name)#跳进去 当前路径

#3.对获取的名字进行重命名
for name in file_names:
    print(name)#for test
    os.rename(name,"[京东出品]-"+name)

#第二种
#for name in file_names:
    #print(name)
#    old_file_name = "./"+folder_name+"/"+name
#    new_file_name = "./"+folder_name+"/"+"[京东出品]-"+name
#    os.rename(old_file_name,new_file_name)
