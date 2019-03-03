#1.打印提示功能
print('-'*20)
print('   名片管理器 V11.01')
print('   1.添加名片')
print('   2.删除名片')
print('   3.修改名片')
print('   4.查询名片')
print('   5.退出系统')
print('-'*20)

names = []
adds = []

#2.获取用户的选择
choice = int(input('请输入您的选择：'))

#3.根据选择执行相应的功能
if choice == 1:
    new_name = input('请输入您的姓名：')
    new_add = input('请输入您的地址：')
    
    names.append(new_name)
    adds.append(new_add)

    print('='*10)
    print('姓名：%s'%names)
    print('地址：%s'%adds)
    print('='*10)






if choice == 2:
    del_name = input('请输入您要删除的名片')





if choice == 3:
    pass
if choice == 4:
    pass
if choice == 5:
    pass














