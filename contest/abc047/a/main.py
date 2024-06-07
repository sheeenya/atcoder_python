a,b,c = map(int,input().split())
ans =""

if a+b==c:
    ans = "Yes"
if a+c==b:
    ans = "Yes"
if c+b==a:
    ans = "Yes"

if ans == "Yes":
    print("Yes")
    exit()

print("No")