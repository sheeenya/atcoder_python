N=int(input())
a=list(map(int,input().split()))

x=0
y=sum(a)
ans=10**20

for i in range(len(a)-1):
    x += a[i]
    y -= a[i]
    if ans > abs(x-y):
        ans = abs(x-y)

print(ans)
