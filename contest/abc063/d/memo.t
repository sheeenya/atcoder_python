N,A,B = map(int,input().split())
h = []

for i in range(N):
    h.append(int(input()))

ans = 0

while max(h) > 0:

    h = [n-B for n in h]
    h[h.index(max(h))] -= (A - B)
    ans += 1

print(ans)

全体にBダメージ与えて、最も体力の高い魔物にはB-Aダメージ与える
これを魔物全て倒すまで繰り返す

魔物が大量、ダメージが小さいときに計算量が多くなりLTE


M回の爆発で魔物を全て倒せるか判定、M回を二分探索法で算出する
※Mの最小の数を一発で求めるのは恐らく不可能