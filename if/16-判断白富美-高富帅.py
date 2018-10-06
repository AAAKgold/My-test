
sex = input('请输入你的性别：')

#如果当前用户是男性的话，那么就输入判断女性的要求
if sex == '男':
    color = input("你白么？")
    money = int(input("请输入你的财产总和："))
    beautiful = input("你美么？")

    if color == '白' and money>100000000 and beautiful == '美':
        print('白富美……')
    else:
        print('矮穷矬……')
else:
    print('判断高富帅的信息在下面')
