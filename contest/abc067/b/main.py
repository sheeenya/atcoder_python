N,K=map(int,input().split())
l=list(map(int,input().split()))

L=sorted(l)
ans =0

for i in range(K):
    ans += L.pop()

print(ans)
