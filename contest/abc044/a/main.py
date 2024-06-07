N = int(input())
K = int(input())
X = int(input())
Y = int(input())

ans = 0

if N <= K:
    print(X*N)
else:
    print(X*K+Y*(N-K))