ticket = input("请问您有车票吗？(1表示有车票，0表示没有车票)") #输入1/0,1代表有票，0代表没有票

#输入刀子长度 并转换变量类型
knifeLength = int(input("请输入刀长:"))

if ticket == "1":
    print("有车票，可以进安检区")


    if knifeLength<10:
        print("通过安检")
        print("终于可以见到Ta了，美滋滋")
    else:
        print("未通过安检")
        print("等待警察处理")
else:
    print("没有车票")
    print("见不到Ta，一票难求")
