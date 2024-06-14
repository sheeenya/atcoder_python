A,B,C = map(str,input().split())

if B[0]==A[-1] and C[0]==B[-1]:
    print("YES")
else:
    print("NO")
