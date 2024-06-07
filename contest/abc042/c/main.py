N,K = map(int,input().split())
D = list(map(int,input().split()))
switch = 1
for i in range(N,100000):
    if switch ==0:
        print(i-1)
        exit()
    
    switch=0
    ilist =[int(digit) for digit in str(i)]
    for j in ilist:
        if j in D:
            switch = 1
            break
        



        


           

"""墓場
N,K = map(int,input().split())
D = list(map(int,input().split()))
Nlist = [int(digit) for digit in str(N)]
ans = 0
cnt = -1
Nlist.reverse()
start = Nlist.copy()
for i in start:
    poppen = int(Nlist.pop(0))
    cnt +=1
    if poppen == 10:
            poppen =0
            if not Nlist:
                Nlist.append(1)
                start.append(1)
            else:Nlist[0] += 1

    while poppen in D:
        poppen += 1
        if poppen == 10:
            poppen =0
            if not Nlist:
                Nlist.append(1)
                start.append(1)
            else:Nlist[0] += 1
    ans += poppen*10**cnt
    

print(ans)
"""
