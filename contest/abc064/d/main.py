N = int(input())
S = input()
ans = S
sum = 0
for i in S:
    if i =="(":
        sum += 1
    else:
        sum -= 1
    if sum == -1:
        ans = "("+ans
        sum += 1

while sum > 0:
    ans = ans + ")"
    sum -= 1

print(ans)



"""
(を+1、)を-1として左から足していく
最後までいったときに0になるように右端に)を追加
途中でマイナスになったら左端に(を追加
"""