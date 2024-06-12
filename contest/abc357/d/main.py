n = int(input())
k = len(str(n)) # nの桁数
p = 998244353
def f(n,i):  # Nをi個繋げた状態
    if i ==1:
        return n%p 
    if i % 2 ==0: # iが2以上の偶数
        t = f(n,i//2)
        #return (t*10**(i//2*k)+t)%p  この書き方だとTLE
        return (t*pow(10,i//2*k,p)+t)%p # tに置き換えない書き方でもTLE
    else: # iが3以上の奇数
        return (f(n,i-1)*10**k+n)%p
print(f(n,n))
        