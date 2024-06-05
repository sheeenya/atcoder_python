W = input()
X = []
for i in W:
    if i in "aiueo":
        continue      
    else:
        X.append(i)
    
print(*X,sep="")
