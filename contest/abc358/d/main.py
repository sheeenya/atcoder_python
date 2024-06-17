N,M=map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

A = sorted(A)
B = sorted(B)

import bisect

ans = 0
idx = 0

for i in A:
    if i >= B[idx]:
        ans += i
        idx += 1
    if idx ==len(B): #popを使ってBの要素を削除しようとすると、pop(0)自体の計算量がO(N)のためTLE
        break

if idx < len(B):
    ans = -1

print(ans)

"""
Bの値でloopして、Aの値でloopとやるとn**2？
Aの値でloopすればBでloopする必要なし
"""
