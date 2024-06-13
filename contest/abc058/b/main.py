O = list(input())
E = list(input())
x=len(O)
ans=[]

for i in range(x):
    ans.append(O.pop(0))
    if len(E) > 0:
        ans.append(E.pop(0))

print("".join(ans))