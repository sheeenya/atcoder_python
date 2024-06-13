n = int(input())
S =[]
ans =""

for i in range(n):
    S.append(input())

if n ==1:
    print("".join(sorted(S[0])))
    exit()

for i in range(len(S)-1):
    ans =""
    for j in range(len(S[i])):
        if (S[i])[j] in S[i+1]:
            f=S[i+1].find((S[i])[j])
            S[i+1] = S[i+1][:f]+S[i+1][f+1:]
            ans += (S[i])[j]
    S[i+1] = ans

print("".join(sorted(ans)))