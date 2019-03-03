knife = input("请输入刀子的长度") #输入刀子的长度

knife_length = int(knife) #变量数据类型转换

if knife_length<10: #if判断刀长
    print("刀子可以带上火车")
else:
    print("刀子不可以带上火车")
