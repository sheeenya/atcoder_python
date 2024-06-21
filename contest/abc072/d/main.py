N=int(input())
p=list(map(int,input().split()))

m=0
cnt=0
for i in range(1,N):
    if i==p[i-1]:
        m=p[i-1]
        p[i-1]=p[i]
        p[i]=m
        cnt +=1

if p[N-1]==N:
    m=p[N-2]
    p[N-2]=p[N-1]
    p[N-1]=p[N-2]
    cnt +=1
print(cnt)

"""
左からみていって被っていたら右といれかえる
"""