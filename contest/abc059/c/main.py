n = int(input())
a = list(map(int,input().split()))
SumI = 0
ansO = 0
ansE = 0

#奇数を正にする場合
for i in range(n):
    SumI += a[i]
    if i%2 == 0: #奇数項
        if SumI <= 0:  
            ansO += 1-SumI
            SumI = 1
    else:   #偶数項
        if SumI >= 0:
            ansO += 1+SumI
            SumI = -1

SumI = 0

#偶数を正にする場合
for i in range(n):
    SumI += a[i]
    if i%2 != 0: #奇数項
        if SumI <= 0:  
            ansE += 1-SumI
            SumI = 1
    else:   #偶数項
        if SumI >= 0:
            ansE += 1+SumI
            SumI = -1

print(min(ansO,ansE))

"""
偶数番目と奇数番目、どちらを正にするかは試行すればよい
2通りでしかないので、どちらも試して小さい方を採用する
"""