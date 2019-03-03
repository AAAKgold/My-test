def printLine(row):
    for col in range(1,row+1):
        print("%d*%d=%d\t"%(col,row,col*row),end=" ")
    print("")

for row in range(1,10):#左闭右开
    printLine(row)


