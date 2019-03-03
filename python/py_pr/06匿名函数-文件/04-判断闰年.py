def judgeLeap_year():
    #1.用户的输入
    year = int(input("请输入年份："))

    #2.判断是否是闰年
    if year%400 == 0:
        print("%d是闰年"%year)
    elif year%4 == 0 and year%100 != 0:
        print("%d是闰年"%year)
    else:
        print("%d不是闰年！"%year)
judgeLeap_year()


