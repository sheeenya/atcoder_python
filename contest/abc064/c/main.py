N = int(input())
a = list(map(int,input().split()))
val = []
free = 0

for i in a:
    if i > 3199:
        free += 1
    else:
        val.append(i//400)

print(str(max(1,len(set(val))))+" "+str(len(set(val))+free))