n,a,b = map(int,input().split())
x = list(map(int,input().split()))
now = 0
ans = 0

for i in range(len(x)):
    if i == 0:
        now = x[i]
    else:
        ans += min((x[i]-now)*a,b)
        now = x[i]

print(ans)