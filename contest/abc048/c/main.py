N,x = map(int,input().split())
a = list(map(int,input().split()))
ans = 0
for i in range(N):
    if i ==0:
        if a[i] > x:
            ans += a[i]-x
            a[i] = x          
    else:
        if a[i]+a[i-1] > x:
            ans += a[i]-x+a[i-1]
            a[i] = x-a[i-1]        
print(ans)
