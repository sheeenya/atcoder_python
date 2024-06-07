N = int(input())
ans = 0
T = 0
A = 0

def ceil_division(a,b):
    if a% b ==0:
        return a // b
    else:
        return a//b + 1

for i in range(N):
    Tin,Ain = map(int,input().split())   
    if i == 0:
        T = Tin
        A = Ain
    else:
        if Tin >= T and Ain >= A:
            T = Tin
            A = Ain
        else:
            T = Tin*max(ceil_division(T,Tin) , ceil_division(A,Ain))
            A = Ain*max(ceil_division(T,Tin) , ceil_division(A,Ain))
print(T+A)