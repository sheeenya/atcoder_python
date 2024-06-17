N,M = map(int,input().split())
S =[]
total =[]
for i in range(N):
    S.append(input())

ans = 10000

for i in range(2**N):
    total =[]
    for j in range(N):
        if (i>>j) & 1:
            total.append(S[j])
    
    for l in range(M):
        jdg =[]
        for k in total:
            jdg.append(k[l])
        if  not "o" in jdg: #jdgの中に o が含まれていない場合は次のiまで行きたい
            break
    else: #forでelseを使うと、ループが最後まで実行されたときのみに実行される
        ans = min(len(total),ans)

print(ans)    


"""
bit全探索を用いる、N個の売り場について、訪れる売り場のパターンを全探索
（N=3 なら、000,001,010,011,100,101,110,111 のように）2^^N通りとなる
それぞれのパターンにて全てのフレーバーを購入できるかチェック、最終的に、訪れる売り場の数が最も小さいときの数字を出力
"""