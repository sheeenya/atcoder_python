N=int(input())
a=sorted(list(map(int,input().split())))

#数字と個数の組み合わせを示す2次元リストを作る
alist=[[i,0] for i in range(max(a)+1)]

for i in a:
    alist[i][1] += 1

ans=[]

if len(alist) ==1:
    for j in range(len(alist)):
        ans.append(alist[j][1])

elif len(alist) ==2:

    for j in range(len(alist)-1):
        ans.append(alist[j][1]+alist[j+1][1])

else:

    for j in range(len(alist)-2):
        ans.append(alist[j][1]+alist[j+1][1]+alist[j+2][1])

print(max(ans))

"""
O(N)の回数は問題にならない
Nをソートしたり、Nについて、各数字の個数を調べるのは問題ない

"""


"""
参考にしたいスマート解答

n=int(input())
a=list(map(int,input().split()))
b=[0]*(10**5+2)
for i in range(n):
  b[a[i]+1]+=1
  b[a[i]]+=1
  b[a[i]+2]+=1
print(max(b))

"""