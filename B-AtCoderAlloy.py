cnt=0
N, H, W = map(int, input().split())
for i in range(N):
    a, b = map(int, input().split())
    if a >= H and b >= W : cnt+=1
 
print(cnt)
