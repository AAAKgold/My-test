i = 1
while i<=10:
    i+=1

    print('-----')

    if i==3:
        #break #结束整个循环
        continue #这一次的循环结束，下面的代码不执行 即print(i)不执行

    print(i)

print('=====')
