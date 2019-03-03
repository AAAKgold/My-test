#在Python中 值是靠引用来传递
# id() 判断两个变量是否为同一个值的引用  id可理解为内存的地址标示

a = 1
b = a
print(id(a))
print(id(b))


a = 2
print(id(a))

