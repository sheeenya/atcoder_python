Wmax,Hmax,N = map(int,input().split())
Wmin =0
Hmin =0
AW = Wmax*Hmax

for i in range(N):
    x,y,a =map(int,input().split())
    if a ==1 and Wmin<x:
        Wmin=x
    elif a ==2 and Wmax>x:
        Wmax=x
    elif a ==3 and Hmin<y:
        Hmin=y
    elif a ==4 and Hmax>y:
        Hmax=y

if Hmax > Hmin and Wmax > Wmin:
    print((Hmax-Hmin)*(Wmax-Wmin))
else:
    print(0)
