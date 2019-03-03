import os
#1.获取用户文件夹输入
file_name = input("请输入您要重命名的文件夹：")


#2.获取所有文件名
file_names = os.listdir(file_name)
#print(file_names) #for test

#第一种方法
#os.chdir(file_name) #跳进当前目录才能重命名

#3.修改文件名
#for name in file_names:
#    os.rename(name,"[东哥出品]-"+name)

#第二种


for name in file_names:
    old_name = "./"+file_name+"/"+name
    new_name = "./"+file_name+"/"+"[东哥出品]-"+name
    os.rename(old_name,new_name)





