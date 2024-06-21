N=int(input())
abc=[]
for i in range(N-1):
    abc.append(list(map(int,input().split())))

print("abc = ",end="")
print(abc)

Q,K=map(int,input().split())

xy=[]
for j in range(Q):
    xy.append(list(map(int,input().split())))

print("xy = ",end="")
print(xy)

print("K = ",end="")
print(K)

cost=[] #Kから各点への距離を示す(ex. 3,8　→Kから点3へは距離8)

#costを再帰関数にて深さ優先探索で求める
ori=K #距離を求める起点
dis=0 #距離

def f(N):
    if N ==


"""
Kから各点への距離を求める
abcからKを含むものを抽出、


"""