N = int(input())
s = []

for i in range(N):
    s.append(int(input()))
sort_s = sorted(s)
S = sum(s)
if S%10 != 0:
    print(S)
else:

    for i in range(N):
        if sort_s[i]%10 != 0:
            print(S - sort_s[i])
            exit()

    else:
        print(0)

"""
まず全て合計した場合に10の倍数かどうか
10の倍数であれば、10の倍数でないもののうち最小の値を引けば終了
"""