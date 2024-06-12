N=int(input())
PFlist =[]

if N == 1: #コーナーケース
    print(1)
    exit()

def prime_factoriza(n): # nの素因数分解、出力はリスト
    a =[]
    while n % 2 ==0: # 2を取り出す
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f ==0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

for i in range(1,N+1):
    PFlist += prime_factoriza(i)   

PFlist.sort()
ans=0
math="1"
for i in range(1,len(PFlist)):
    if PFlist[i] == PFlist[i-1]:
        ans +=1
    else:
        ans +=2
        math += "*"+str(ans)
        ans =0

ans +=2
math += "*"+str(ans)
print(eval(math)%1000000007)

"""
解説より
ある整数xが素因数分解によってp**n*q**m*...と表せるとき、
xの約数の個数は(n+1)*(m+1)*...となる
x=720
2^4*3^2*5^1
5*3*2
30


N!の素因数分解を行う

"""

