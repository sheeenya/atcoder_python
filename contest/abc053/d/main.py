n = int(input())
a = list(map(int,input().split()))
a.sort()
cnt =1

now = a[0]
for i in range(len(a)):
    if i ==0:
        continue
    if a[i] !=a[i-1]:
        cnt +=1

if cnt%2 ==0:
    print(cnt-1)
else:
    print(cnt)

"""
数字の種類をnとし、nが偶数ならn-1、nが奇数ならnが答え？
"""