def sum_2_nums(a,b,*args):#  * + 形参 = 不定长参数 
    print("-"*30)
    print(a)
    print(b)
    print(args)

    result = a+b
    for num in args:
        result = result + num

    print("result=%d"%result)





sum_2_nums(11,22,33,44,55)
sum_2_nums(11,22,33)
sum_2_nums(11,22)
