N,K = map(int,input().split())
L =[]
sum =0

for i in range(N):
    L.append(list(map(int,input().split())))

SortedL = sorted(L) 

for i in range(N):
    sum += SortedL[i][1] #SortedLに置き換えないでやってるとTLE
    if sum >= K:
        ans = SortedL[i][0]
        break

print(ans)


"""
2次元のリストをソートして、bをNまでたしていきK以上になった時点のaを求める
"""




"""
気合でやるとLTE

for i in range(N):
    a,b = map(int,input().split())
    for j in range(b):
        L.append(a)

print(sorted(L)[K-1])

"""