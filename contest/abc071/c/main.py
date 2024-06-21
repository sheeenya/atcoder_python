N=int(input())
A=list(map(int,input().split()))

SortA=sorted(A)
p=0
cnt = 0
for i in range(len(SortA)):
    if p==SortA[-1]:
        if cnt ==1:
            print(x*SortA.pop())
            exit()
        else:
            x = SortA.pop()
            p = 0
            cnt +=1

    else:
        p=SortA.pop()

print(0)

