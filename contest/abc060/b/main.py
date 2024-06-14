A,B,C = map(int,input().split())

for i in range(B):
    if A*(i)%B == C:
        print("YES")
        exit()
else:
    print("NO")

"""
Aの倍数をどれだけ選んでもAの倍数になることは変わらない
また、(A*B)%B=0 のため
A%B=(A*B+A)%B であり、AからA*Bまでを調べればよい→全探索

"""