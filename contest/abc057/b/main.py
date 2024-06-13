N,M = map(int,input().split())
alist =[]
blist =[]
clist =[]
dlist =[]
dist = 10000000000
ans =0

for i in range(N):
    a,b = map(int,input().split())
    alist.append(a)
    blist.append(b)

for i in range(M):
    c,d = map(int,input().split())
    clist.append(c)
    dlist.append(d)

for i in range(N):
    dist = 10000000000
    for j in range(M):
        x = abs(alist[i]-clist[j])+abs(blist[i]-dlist[j])
        if x <dist:
            dist =x
            ans =j+1
    print(ans)

