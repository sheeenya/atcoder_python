N,M=map(int,input().split())
alist=[]
blist=[]

for i in range(M):
    a,b=map(int,input().split())
    if a==1:
        alist.append(b)
    elif b==N:
        blist.append(a)

if set(alist)&set(blist) == set():
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")




"""
Nから行ける島を調べ、1いから行ける島がそこに含まれればOK
"""