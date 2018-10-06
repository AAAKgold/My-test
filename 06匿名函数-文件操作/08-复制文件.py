#1. 获取要复制的文件名
old_file_name = input("请输入要复制的文件（需要后缀）：")

#2.打开要复制的文件
f_read = open(old_file_name,"r") #此处读取文件不用引号，因为input本是字符串类型

#假如原文件名为：test.txt  ------>test[复件].txt
#new_file_name = old_file_name+"[复件]" #此法可以 ，low

#new_file_name = old_file_name.rreplace(".","[复件.]"，1)#想法好， 没有rreplace 报错

position = old_file_name.rfind(".")
new_file_name = old_file_name[0:position] + "[复件]" + old_file_name[position:]#切片

#3.创建一个新的文件
f_write = open(new_file_name,"w")


#4. 从old文件中读取数据，写入到new文件中
#content = f_read.read()#读大文件内存不够
#f_write.write(content)

while True:
    content = f_read.read(1024)#读大文件一次读1024字节
    if len(content)==0:
        break
    f_write.write(content)

#5. 关闭两个文件
f_read.close()
f_write.close()



