N=int(input())

for i in range(10):
    if 2**i <= N:
        ans = 2**i
    
print(ans)