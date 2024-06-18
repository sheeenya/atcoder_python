r,g,b = map(int,input().split())
st = str(r)+str(g)+str(b)
inte = int(st)

if inte%4==0:
    print("YES")
else:
    print("NO")
