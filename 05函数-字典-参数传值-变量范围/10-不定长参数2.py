def test(a,b,c=33,*args,**kwargs):
   print(a)
   print(b)
   print(c)
   print(args)
   print(kwargs)



#test(11,22,33,44,55,66,77,task=99,done=89) 


A = (44,55,66)

B = {"name":"laowang","age":18}


test(11,22,33,*A,**B) #拆包
