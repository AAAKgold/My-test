name = 'xiaoming'
position = '讲师'
address = '北京市昌平区建材城西路金燕龙办公楼1层'

'''
print('-'*50)
print('姓名：%s'%name)
print('职位：%s'%position)
print('公司地址：%s'%address)
print('-'*50)
'''

'''
print(name[-1]) #取倒数第一个字符 即最后一个字符

#切片：

print(name[0:2]) #取 下标0~2的字符  左闭右开原则  

print(name[2:]) #取 下标为2开始到最后的字符  

print(name[1:-2]) #取 下标为1开始 到最后倒数第2个 之间的字符

print(name[:-2]) #取 下标为0开始 到最后倒数第2个 之间的字符

print(name[::2]) #从0开始取到最后 下标以2为间隔

print(name[2:7:3]) #从下标为2开始 取到下标为6 间隔为3

print(name[::-2]) #从最后取 到0 间隔为2  实际上负号就是倒着取
'''

print(name[5:0:-2]) #取下标从0~5 间隔为2 倒着取



