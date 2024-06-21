K=int(input())

N = 50
print(N)

y=K//50+(50-K%50-1)
x=N+(K-1)//N

print((str(x)+" ")*(K%N)+(str(y)+" ")*(N-K%N))
