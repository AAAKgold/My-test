#encoding=utf-8

#1. len()#测量字典中 键值对 的个数
'''
dict = {'name':'zhangsan','sex':'m'}
print(len(dict))
'''

#2.keys#返回一个包含字典所有KEY的列表
'''
dict = {'name':'zhangsan','sex':'m'}
print(dict.keys())
'''

#3.values#返回一个包含字典所有value的列表
'''
dict = {'name':'zhangsan','sex':'m'}
print(dict.values())
'''


#4.items #返回一个包含所有（键、值）元组的列表
'''
dict = {'name':'zhangsan','sex':'m'}
print(dict.items())
'''

#5.has_key #如果key在字典中 返回True 否则返回False
'''
dict = {'name':'zhangsan','sex':'m'}
print(dict.has_key('name'))#只有Python2能用has_key 注意前面要utf-8
print(dict.has_key('phone'))
'''




