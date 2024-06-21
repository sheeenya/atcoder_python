N=int(input())
a=list(map(int,input().split()))
x4cnt=0
x2cnt=0

for i in a:
    if i%4==0:
        x4cnt+=1
    elif i%2==0:
        x2cnt+=1

if x4cnt+x2cnt//2 >= N//2:
    print("Yes")
else:
    print("No")


"""
4の倍数の数と
2の倍数の数x2
を合計して、len(N)の半分あればよい
"""