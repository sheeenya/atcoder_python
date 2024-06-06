N = int(input())
a = list(map(int,input().split()))
ans = 0
for i in a:
    ans += (round(sum(a)/N) - i)**2
print(ans)