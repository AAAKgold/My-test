def test(a,d,b=22,c=33):# b c 缺省参数  ;a  d 不是缺省参数 
    print(a)
    print(b)
    print(c)
    print(d)

test(11,22,c=44)# c 命名参数
#test(d=11,a=22,c=44)
