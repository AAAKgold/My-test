#通过for……in…… 
'''
#1.字符串遍历
a_str = 'hello itcast'
for char in a_str:
    print(char,end=' ')

#2.列表遍历
a_list = [1,2,3,4,5]
for num in a_list:
    print(num,end=' ')

#3.元组遍历
a_turple = (1,2,3,4,5)
for num in a_turple:
    print(num,end=' ')
'''

'''
#4.字典遍历
#<1>遍历字典的key（键）
dict = {'name':'zhangsan','sex':'m'}
for key in dict.keys():
    print(key)#python3必须括号输出  

#<2>遍历字典的value（值）
dict = {'name':'zhangsan','sex':'m'}
for value in dict.values():
    print(value)#python3必须括号输出  

#<3>遍历字典的项(元素)
dict = {'name':'zhangsan','sex':'m'}
for item in dict.items():
    print(item)



#<4>遍历字典的key-value (键值对)
dict = {'name':'zhangsan','sex':'m'}
for key,value in dict.items():
    print('key=%s,value=%s'%(key,value))

#5.带下标索引的遍历
chars = ['a','b','c','d']
i = 0
for char in chars:
    print('%d %s'%(i,char))
    i+=1

#enumerate()
chars = ['a','b','c','d']
for i,char in enumerate(chars):
    print(i,char)
'''

#6.公共方法 运算符

#注意 in在对字典操作时，判断的是字典的键
print('name' in {'name':'Delron','age':24})










