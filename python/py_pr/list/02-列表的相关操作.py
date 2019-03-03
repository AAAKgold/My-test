'''
A = ['xiaoWang','xiaoZhang','xiaoHua']
print('===操作之前，列表A的数据===')
for tempName in A:
    print(tempName)
'''

#1.添加元素

#list.append() 在末尾添加
'''
temp = input('请输入要添加的姓名：')
A.append(temp)
print('===操作之后，列表A的数据===')
for tempName in A:
    print(tempName)
'''

#extend 可以将另一个集合中的元素逐一添加到列表中
'''
a = [1,2]
b = [3,4]
a.extend(b)
'''


#insert(index,object) 在指定位置index前插入元素object
'''a = [0,1,2]
a.insert(1,3)#在下标为1的位置前插入元素 3
print(a)
'''

#2.修改元素
'''
A = ['1','g','f','9']
A[1] = 'hahaha'
print(A)
'''

#3.查找元素
'''
#in 或者 not in
if findName in namelist:  
    print("找到啦哈哈哈")
else:
    print("没找到呜呜呜")
'''

#index 
'''
a = ['f','a','b','c','a','b']
a.index('a',2,4)#左闭右开
'''
#count
'''
a.count('a')
'''



#4.删除元素
'''
#del 根据下标进行删除
del moveName[2]#删除下标为2 的元素的值

#pop 删除最后一个元素
moveName.pop#删除末尾

#remove 根据元素的值进行删除
moveName.remove('指环王')#删除 指环王
'''

#5.sort reverse
'''
a = [1,4,2,3]

a.reverse()#将list逆置

print(a)

a.sort()#将list按特定顺序默认为从小到大， 参数reverse=Ture 可改为倒序 即由大到小

print(a)
'''


#6. strip #去除
a = "\rzh ang\n\t san "
print(len(a))

#b = a.strip(" ")
b = a.strip()
print(b)







