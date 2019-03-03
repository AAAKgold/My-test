from math import sqrt

def judgePrime(num):
    if num <= 1:
        return 0
    #for i in range(2,int(sqrt(num)+1)):
'''    for i in range(2,num):#此两种算法皆可，上面比下面快很多，找素数只需要除到平方根+1
        if num%i == 0:
            return 0
    return 1
'''
    i = 1#有问题
    while i*i <= num:
        if num%i == 0:
            return 0
    i += 1
    return 1




j = 1
for a in range(0,100000):
    if judgePrime(a) == 1:
        #print(a)
        j += 1
    
print("素数的个数是:%d"%j)



