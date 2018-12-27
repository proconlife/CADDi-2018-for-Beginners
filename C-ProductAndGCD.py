import math
 
n,p=map(int,input().split())
 
def C(N,P):
    if N == 1: return P
    b=int(math.log2(N))
    a=int(P**(1/b))+2
 
    res=1
    for i in range(2,a):
        c=i**N
        if c > P : break
        if P % c == 0 : res = i
 
    return res
 
print(C(n,p))
