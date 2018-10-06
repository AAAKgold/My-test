#递归
'''
i= 1
result = 1
while i <= 4:
    result *= i
    i += 1
print(result)
'''

'''
def xx(num):
    num * xxx(num-1)


def getNums(num):
    num * xx(num-1)



getNums(4)
'''

def getNums(num):
    if num > 1:
        return num * getNums(num-1)#return 返回值
    else:
        return num 


result = getNums(4)

print(result)






