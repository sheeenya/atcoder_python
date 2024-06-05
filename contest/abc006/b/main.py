n = int(input())
X = 0
a1 = 0
a2 = 0
a3 = 0


for i in range(n):
    if i == 0:
        X = 0
    elif i == 1:
        X = 0
    elif i == 2:
        X = 1
    else:
        a1 = a2
        a2 = a3
        a3 = X
        X = (a1 + a2 + a3) % 10007

print(X)
