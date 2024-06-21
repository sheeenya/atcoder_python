n = int(input())
a = list(map(int,input().split()))
b = []

for i in range(n):
    if n > i*2:
        b.append(a[n-i*2-1])
    else:
        if n%2 ==0:
            b.append(a[(i-n//2)*2])
        else:
            b.append(a[(i-n//2)*2-1])


b = list(map(str,b))
print(" ".join(b))

"""
素直にやるとLTE
for i in range(n):
    b.append(a[i])
    b.reverse()
reverse の計算量がO(N)

reverseを使わずに実装する
"""
