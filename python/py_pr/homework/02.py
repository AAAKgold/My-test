i = 1
num = int(input("请输入行数："))
while i <= num:
    if i <= num/2:   
        j = 1
        while j <= i:
            print("* ",end='')
            j += 1
          
        print("\n")
        i += 1
    else:
        j = 1
        while j <= num - i:
            print("* ",end='')
            j += 1
          
        print("\n")
        i += 1
