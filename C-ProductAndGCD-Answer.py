n,p = list(map(int,input().split())) 
i = a = o = 1
m = round(p**(1/n))
for i in range(m,0,-1):
    a = i**n
    if p%a==0:
        print(i)
        exit()
