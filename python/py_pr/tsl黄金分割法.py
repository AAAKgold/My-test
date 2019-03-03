#黄金分割法确定单峰函数在区间的极小点
#0.618法求解IRR的应用举例
import math

#定义内部收益率函数
def NPV(x):
    return -300+96*(pow(1+x,5)-1)/(x*pow(1+x,5))
#print(NPV(0.1)) #for test

#定义主函数 黄金分割法计算
def main(i0,j0,l):#区间和精度
    global x_ans 
    global NPV_ans  
    global k
    r = 1 - (math.sqrt(5)-1)/2
    k = 0
    i1 = i0+r*(j0-i0)
    j1 = i0+(1-r)*(j0-i0)
    #循环分割 if判断
    while abs(j0-i0) > l:
        k += 1
        N1 = NPV(i1)
        N2 = NPV(j1)
        if N1 >= N2:
            i0 = i1
            i1 = j1
            N1 = N2
            j1 = i0+(1-r)*(j0-i0)
        else:
            j0 = j1
            j1 = i1
            N2 = N1
            i1 = i0+r*(j0-i0)
        x_ans = (i0+j0)/2
        NPV_ans = NPV(x_ans)
    return (x_ans,NPV_ans,k)
    #print(i0,j0)#for test

main(0.1,0.2,0.001)#初值区间[10%,20%] l为精度 r为压缩比
print("%.3f 是极小值点，迭代了%d次，NPV取值为%.3f"%(x_ans,k,NPV_ans))

