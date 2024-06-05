N,L,R = map(int,input().split())
X =[]
A = []

for i in range(N):
    A.append(i+1)

for i in range(N):
    if i+1 == L:
         X.append(R)
    elif i+1 > L and i+1 < R:
        X.append(R-i+L-1)
    elif i+1 ==R:
        X.append(L)
    else:
        X.append(i+1)

print(*X)