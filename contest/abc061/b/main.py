N,M = map(int,input().split())
list =[]

for i in range(M):
    a,b = map(int,input().split())
    list.append(a)
    list.append(b)

for i in range(N):
    print(list.count(i+1))


