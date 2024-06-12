n=input()
s=input()
cnt=0
ans=0

for i in s:
    if i == "I":
        cnt +=1
        if cnt > ans:
            ans=cnt
    else:
        cnt -=1

print(ans)
