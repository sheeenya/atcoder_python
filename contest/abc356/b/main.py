N,M = map(int,input().split())
A = list(map(int, input().split()))
X =[]
sum =[0]*M

for i in range(N):
    X.append(list(map(int, input().split())))

for j in range(M):
    for k in range(N):
        sum[j] += X[k][j]

for l in range(len(sum)):
    if sum[l] < A[l]:
        print("No")
        exit()

print("Yes")
