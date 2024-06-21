N = int(input())
a = []

for i in range(N):
    a.append(int(input()))

j = a[0]
ans = 1

while j != 2: #ボタン2が光っていない
    j = a[j-1]
    ans += 1
    if ans > 10**5:
        print(-1)
        exit()

print(ans)