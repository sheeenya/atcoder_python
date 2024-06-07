a,b,x = map(int,input().split())
ans = 0
hoge = 0

amari =b%x

if amari ==0:
    print((b-a)//x+1)
else:
    hoge = b - amari
    if hoge < 0:
        print(0)
        exit()
    print((hoge-a)//x+1)

#b以下での数からa以下での数を引くのがスマートだった
