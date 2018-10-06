i = 1
while i<=9:
    j = 1
    while j<=i:
        print("%d*%d=%d\t"%(j,i,j*i),end='')  # end='' 不换行 \t 表示对齐，相当于Tab
        j+=1

    print('\n') #换行 
    i+=1

