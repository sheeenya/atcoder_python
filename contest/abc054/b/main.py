n,m = map(int,input().split())
a=[]
b=[]

for i in range(n):
    a.append(input())
for i in range(m):
    b.append(input())

for i in range(n-m+1):
    for x in range(n-m+1):
        j = str(a[i])[x:x+m].find(b[0])

        if j>=0:
            for k in range(1,m):
                if  b[k] != str(a[i+k])[x:x+m]:
                    break
                           
            else:
                print("Yes")
                exit()
else:
    print("No")
    exit()

"""
b0が含まれるanを探す
a0内の位置jを返す

    位置jにおいて
    b1とan+1、b2とan+2、bmとan+mが一致すればYes


"""
