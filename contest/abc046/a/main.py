a,b,c = map(int,input().split())

if a == b:
    if a == c:
        print(1)
    else:
        print(2)
elif a == c:
    print(2)
elif b == c:
    print(2)
else:
    print(3)
