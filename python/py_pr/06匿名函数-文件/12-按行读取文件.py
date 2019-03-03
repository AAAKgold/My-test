
#1. 打开文件
fold_name = input("请输入您要打开的文件名：")
file_name = open(fold_name,"r")

#2. 读取全部内容
content = file_name.readlines()
#print(content) #for test
#3.遍历 去除以空格开头的行的空格， 然后去除以#开头的行的#号
for i in content:
    #print(i)#for test
    i.strip(" ")#至关重要
    if i[0] == "#":
        continue
    else:
        print(i)

#print(content)

file_name.close()

