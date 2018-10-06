#a1 = '老王'
#a2 = '老李'
#a3 = '老刘'
#列表 
#names = ['老王','老李','老刘']#定义一个列表

#nums = ['laowang','laoli',11,22,3.14]#可存储不同类型数据


#增删改查

#names.append('老赵')  #增加 从最后一个曾增加 栈

#names.insert(位置，要添加的内容)
#names.insert(0,'八戒')
#names.insert(2,'沙僧')

#两个列表相加
names2 = ['葫芦娃','叮当猫','猴子']
names = ['老王','老李','老刘']#定义一个列表
names3 = names + names2
names.extend(names3)

print(names) 

