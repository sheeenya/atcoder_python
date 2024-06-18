N,A,B = map(int,input().split())
h = []

for i in range(N):
    h.append(int(input()))

min = 1
max = max(h)//B + 1
ans = (max + min)//2
cnt = 0
import math

while max - min > 1: #二分探索の終わり
    cnt = 0

    for i in h:
        if i > ans*B:
            cnt += math.ceil((i - ans*B)/(A-B))
    
    if cnt > ans: #ansでは足りない
        min = ans + 1
        ans = (max + min)//2
    else: #ansで十分
        max = ans
        ans = math.ceil((max + min)/2)

cnt = 0
for i in h:
    if i > min*B:
        cnt += math.ceil((i - min*B)/(A-B))

if cnt > min: #ansでは足りない
    print(max)
else: #ansで十分
    print(min)

"""
必要な爆発の回数ansを二分探索で求める
まずansが取りうる最小と最大の数を求める（大体でいいので）
最小は1でいいや
最大は魔物の体力の最大値/B
最小と最大の平均を初期値とする
"""


