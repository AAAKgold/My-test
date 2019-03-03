def judge_day():
    '''用来输入年月日判断这一天是这一年的第几天'''
    a = [[31,28,31,30,31,30,31,31,30,31,30,31],[31,29,31,30,31,30,31,31,30,31,30,31]]
    #1.用户输入年月日
    year = int(input("请输入需要判断的年："))
    month = int(input("请输入需要判断的月："))
    day = int(input("请输入需要判断的日："))

    #2.判断是这一年的第几天
    sum = 0
    if year%4 == 0 and year%100 != 0 or year%400 == 0:
        for i in range(1,month):
            sum = sum + a[1][i]
    else:
        for i in range(1,month):
            sum = sum + a[0][i]
    sum += day

    #3.输出
    print("%d年%d月%d日是这一年的第%d天"%(year,month,day,sum))

    #print(a[1][2])#for test

judge_day()





