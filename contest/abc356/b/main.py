N,M = map(int,input().split())
A = list(map(int, input().split()))
X =[]

for i in range(N):
    i = list(map(int, input().split()))
    
    for j in range(M):
        X[j] += i[j]

print(X)