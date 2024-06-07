w = input()

S = sorted(w)

if len(S)%2 !=0:
    print("No")
    exit()

for i in range(0,len(S),2):
    if S[i] != S[i+1]:
        print("No")
        exit()
    
print("Yes")