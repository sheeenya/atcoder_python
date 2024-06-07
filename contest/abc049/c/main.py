S = input()
SL = list(S)
T =""
word =["dream","dreamer","erase","eraser"]
wd =""
for i in range(len(S)):
    wd = SL.pop(-1) + wd
    if(wd in word):
        wd=""
if wd =="":
    print("YES")
else:
    print("NO")