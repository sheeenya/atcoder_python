n = int(input())

p = 1

def train(n):
    mod = 10**9+7
    result = 1
    for i in range(2,n+1):
        result = (result*i)%mod
    return result
print(train(n))
