#1.修改元素
'''
info = {'name':'班长','id':'100','address':'地球亚洲大陆'}
newID = input('请输入新的学号：')

info['id'] = int(newID)#修改
print('修改之后的id为%d'%info['id'])
'''

#2.添加元素
'''
info = {'name':'班长','sex':'f','address':'地球亚洲大陆'}
newID = input('请输入你的学号：')

info['id'] = newID#添加
print('添加之后的id为：%s'%info['id'])
'''

#3.删除元素

#del 删除指定的元素
'''
info = {'name':'班长','sex':'f','address':'地球亚洲大陆'}
print('删除前，%s'%info['name'])
del info['name']#删除
print('删除后，%s'%info['name'])#删除后不能访问
'''

#del 删除整个字典
'''
info = {'name':'班长','sex':'f','address':'地球亚洲大陆'}
print('删除前，%s'%info)
del info
print('删除后，%s'%info)#删除后不能访问
'''

#clear 清空整个字典
'''
info = {'name':'班长','sex':'f','address':'地球亚洲大陆'}
print('清空前，%s'%info)

info.clear()

print('清空后，%s'%info)
'''


info = {'name':'班长','id':'100','address':'地球亚洲大陆'}
newID = input('请输入新的学号：')

info['id'] =int(newID)#修改
print('修改之后的id为%d'%info['id'])
print(info['id'])













































