import math
import functools
N=int(input())
T=[]
for i in range(N):
    T.append(int(input()))
T = set(T)
def my_lcm_base(x,y):
    return (x*y)//math.gcd(x,y)
def my_lcm(*integers):
    return functools.reduce(my_lcm_base, integers)
print(my_lcm(*T))
