N,M = map(int,input().split())

if abs(N-M) > 1:
    print(0)
    exit()

# i の階乗を行う
def f(i):
    result = 1
    for i in range(1, i+1): # 再帰関数にするとN,Mが大きすぎるときにエラー forならOK
        result = result * i %(10**9+7) #途中で余りにしないとLTE
    return result

if N == M:
    print(f(N)*f(M)*2%(10**9+7))
else:
    print(f(N)*f(M)%(10**9+7))
